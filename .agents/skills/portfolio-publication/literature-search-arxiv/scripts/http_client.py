# Copyright 2026 Google LLC
# Licensed under the Apache License, Version 2.0

import os
import time
import urllib.request
import urllib.parse
import urllib.error
import tempfile
import gzip

class HttpClient:
    def __init__(self, base_url, qps=1.0 / 3.0, **kwargs):
        self.base_url = base_url
        self.interval = 1.0 / qps if qps > 0 else 0.0
        hostname = urllib.parse.urlparse(base_url).hostname or "arxiv"
        self.lock_file = os.path.join(tempfile.gettempdir(), f"arxiv_rate_limit_{hostname}.txt")

    def _wait(self):
        if self.interval <= 0:
            return
        now = time.time()
        sleep_time = 0
        if os.path.exists(self.lock_file):
            try:
                with open(self.lock_file, "r") as f:
                    last_time = float(f.read().strip())
                elapsed = now - last_time
                if elapsed < self.interval:
                    sleep_time = self.interval - elapsed
            except Exception:
                pass
        if sleep_time > 0:
            time.sleep(sleep_time)
        try:
            with open(self.lock_file, "w") as f:
                f.write(str(time.time()))
        except Exception:
            pass

    def fetch_bytes(self, url, **kwargs):
        self._wait()
        
        # Build request with custom User-Agent
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "SrujanaShodhaArxivSkill/2.0 (mailto:sanjay.chitnis@reva.edu.in)",
                "Accept-Encoding": "gzip"
            }
        )
        
        with urllib.request.urlopen(req, timeout=60) as response:
            content = response.read()
            encoding = response.headers.get("Content-Encoding", "")
            if "gzip" in encoding:
                content = gzip.decompress(content)
            return content
