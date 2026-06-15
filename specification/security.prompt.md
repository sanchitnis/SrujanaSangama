```markdown
# Specification: Secure Agentic Skill Format (SASF) for SrujanaSangama
**Version:** 1.0.0  
**Status:** Proposal  
**Authors:** Architecture Review Board  

---

## 1. Executive Summary
The **SrujanaSangama** multi-agent ecosystem requires a decentralized, secure, and performant mechanism to store, index, and execute autonomous skills (Standard Operating Procedures, system prompts, and tool executable code). Because these files sit on local developer environments and network shares, they present a high-risk vector for tampering and malicious injection. 

This specification defines a hybrid document container that combines **clear-text YAML frontmatter** for fast, local IDE indexing with an **Authenticated Encryption with Associated Data (AEAD)** payload powered by **JSON Web Encryption (JWE)**. By binding the clear-text metadata directly to the cryptographic verification layer as Additional Authenticated Data (AAD), this format ensures absolute integrity and confidentiality without penalizing local file parser performance.

---

## 2. Architectural Design Goals
* **Zero-Knowledge Routing:** Local orchestrators and IDE background workers must be able to scan structural metadata (IDs, requirements, permissions) instantly without spinning up cryptographic processors or possessing private keys.
* **Cryptographic Tamper-Resistance:** No user, malicious script, or intermediate process should be able to alter either the clear-text metadata parameters or the hidden tool logic without invalidating the document.
* **Strict In-Memory Execution:** Decrypted instructions, prompts, or code blocks must live exclusively in transient memory (RAM) and never be written back to local disks.

---

## 3. Document Wire Format
A `.sasf` (SrujanaSangama Agentic Skill File) or standard `.yaml` compliance container is structurally split into two primary zones using standard markdown/YAML triple-dash (`---`) delimiters.

```text
---
[Clear-Text YAML Metadata Block]
---
[Base64URL-Encoded JWE Compact Serialization String]

```

### 3.1 Syntax Layout Example

```yaml
---
skill_id: "reva-academic-evaluator"
version: "2.1.0"
author: "SrujanaSangama Core"
required_permissions: ["read:syllabus", "write:evaluation_report"]
target_runtime: "python-edge-sandbox"
key_id: "rsa-key-2026-v1"
---
eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.c29tZS1rZXktZW5jcnlwdGVkLXN0dWZm.dmVjdG9y.ZEncY3J5cHRlZC1kZXNjcmlwdGlvbi1hbmQtY29kZS1nb2VzLWhlcmU.YXV0aGVudGljYXRpb24tdGFn

```

---

## 4. Cryptographic Lifecycle & Pipeline

The system enforces an asymmetric cryptographic envelope (Public Key to encrypt/seal, Private Key to decrypt/verify).

### 4.1 Authoring & Sealing (Pipeline / Developer Environment)

1. The developer structures the clear-text parameters in the YAML header.
2. The operational tool instructions (prompts, executable code) are drafted in clear-text.
3. The sealing engine pulls the targeted environment's **Public Key**.
4. The **entire raw string of the clear-text YAML block** is extracted and set as the **Additional Authenticated Data (AAD)** parameter.
5. The engine handles the JWE compact serialization sequence:
* Generates a random symmetric Content Encryption Key (CEK).
* Encrypts the logic payload using `A256GCM` or `A256CBC-HS512`.
* Encrypts the CEK with the asymmetric Public Key (`RSA-OAEP` or `ECDH-ES`).
* Factors the AAD (YAML text) into the final encryption matrix to output the **Authentication Tag**.


6. The file is written to the local disk workspace.

### 4.2 JIT Decryption & Context Binding (Local Runtime Extension)

When an agent invokes a skill inside the environment, the local runtime extension intercepts the call:

```
[Agent Invocation] ──> [IDE Runtime Extension] ──> [Extract Raw YAML String]
                                                            │
                                                   (Passes as JWE AAD)
                                                            │
[Isolated Sandbox] <── [In-Memory Raw Payload] <── [Verify Tag & Decrypt]

```

1. **Header Inspection:** The extension splits the file at the `---` boundary and checks the metadata. If `required_permissions` violate local policy, execution aborts.
2. **Context Verification:** The extension extracts the exact string value of the YAML frontmatter.
3. **Key Retrieval:** The extension requests the decryption private key corresponding to the header's `key_id` from the operating system's native secure keychain.
4. **Decryption and Authentication Check:** The JWE token and the raw YAML text (acting as AAD) are fed into the cryptographic module.
* If an adversary changed a setting in the clear-text YAML (e.g., escalations of authority), the calculated tag will mismatch the JWE Authentication Tag. Decryption **fails instantly**, throwing a `Security Integrity Fault`.


5. **In-Memory Handoff:** Upon successful verification, the decrypted instructions are streamed straight to the LLM context window or a sandboxed runner.

---

## 5. Security & Threat Modeling

* **Metadata Alteration Attack:** Prevented by AEAD design. Any modifications to unencrypted elements cause verification failure during runtime checkouts.
* **Local Shoulder-Surfing / Read Leakage:** Proprietary code or internal prompts remain fully encrypted on disk. An adversary with filesystem access cannot discover the inner workings of the skill without local OS keychain authorization.
* **Malicious Skill Execution:** Once decrypted in memory, any executable logic contained in the description must be constrained to an isolated virtual boundary (e.g., WebAssembly runtimes or locked virtual environments) to enforce zero trust on the host machine.

---

## References

* **JSON Web Encryption (JWE):** RFC 7516 - [Specification for JSON Object Encryption Standards](https://www.rfc-editor.org/info/rfc7516/)
* **Authenticated Encryption with Associated Data (AEAD):** RFC 9771 - [Properties of Authenticated Encryption with Associated Data Algorithms](https://datatracker.ietf.org/doc/rfc9771/)
* **OWASP Agentic Security Patterns:** OWASP Agentic AI Security Project - [Universal Skill Format and Top 10 Protections](https://owasp.org/www-project-agentic-skills-top-10/)

```

```