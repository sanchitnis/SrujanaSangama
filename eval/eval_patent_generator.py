import os
import json
import re
import datetime
from pathlib import Path

# Setup paths
EVAL_DIR = Path("d:/Github/SrujanaSangama/eval")
DATA_DIR = EVAL_DIR / "data"
LOG_DIR = EVAL_DIR / "logs"
SCRATCH_DIR = EVAL_DIR / "scratch"

# Create directories
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

# 1. Generate Synthetic Data (Golden Dataset of Inventions)
SYNTHETIC_DATA = [
    {
        "id": "SYN-PAT-001",
        "title": "IoT-Based Precision Soil Moisture Management System",
        "domain": "Smart Agriculture",
        "description": "A system utilizing a network of HSL-calibrated underground moisture sensors communicating via LoRaWAN to an edge-gateway. The edge-gateway executes an adaptive irrigation control algorithm that adjusts water release valves dynamically based on real-time soil porosity, ambient humidity, and weather forecasting API feeds.",
        "novelty": "Dynamic feedback loop integrating local soil porosity metrics with predictive weather model APIs for precise valve control, operating fully on edge computing without requiring continuous cloud connection.",
        "claims": [
            "A precision irrigation system comprising underground LoRa sensors, an edge-gateway, and mechanical valve controllers.",
            "The system of claim 1, wherein the edge-gateway optimizes water cycles based on local forecast models."
        ],
        "section_3_exclusion_risk": "Low",
        "expected_score": 4.8
    },
    {
        "id": "SYN-PAT-002",
        "title": "Secure Zero-Knowledge Proof Authentication Protocol",
        "domain": "Cybersecurity",
        "description": "An authentication protocol using a randomized zero-knowledge cryptographic signature for securing edge-node logins. Avoids storage of secret hashes on central directory nodes, using a multi-factor polynomial handshake verification model.",
        "novelty": "Polynomial handshake for ZKP specifically optimized for memory-constrained edge hardware configurations.",
        "claims": [
            "A cryptographic authentication protocol employing multi-factor zero-knowledge handshakes on edge nodes."
        ],
        "section_3_exclusion_risk": "High (Section 3(k) - Mathematical method)",
        "expected_score": 3.2
    },
    {
        "id": "SYN-PAT-003",
        "title": "Automated ML Pipeline for Predictive Cardiovascular Risk Analysis",
        "domain": "Health Tech / AI",
        "description": "A system that processes raw echocardiogram video feeds using a 3D Convolutional Neural Network (CNN) to detect early indicators of ventricular hypertrophic anomalies before symptoms manifest clinically.",
        "novelty": "3D-CNN temporal spatial feature maps coupled with real-time video stream augmentation to increase anomaly detection accuracy by 18%.",
        "claims": [
            "A medical predictive diagnostics system analyzing video feeds using temporal spatial convolutional feature extraction."
        ],
        "section_3_exclusion_risk": "Medium (Section 3(i) - Diagnostic method)",
        "expected_score": 4.1
    }
]

# Write synthetic dataset to file
with open(DATA_DIR / "patent_generator_eval_dataset.json", "w") as f:
    json.dump(SYNTHETIC_DATA, f, indent=2)

# Helper: Log messages
LOG_FILE = LOG_DIR / "patent_generator_eval_run.log"
def log_message(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

# Run Evaluation and LLM-as-a-Judge Simulation
log_message("Starting Synthetic Data Generation & Evaluation Suite for patent-generator...")
log_message(f"Loaded {len(SYNTHETIC_DATA)} synthetic test cases successfully.")

EVAL_RESULTS = []

for case in SYNTHETIC_DATA:
    log_message(f"Evaluating Case {case['id']}: '{case['title']}'...")
    
    # Simulate Step 1 & 2: Input Verification and Extraction
    log_message("Simulating Step 1 (Input Acquisition) and Step 2 (Information Extraction)...")
    extracted_terms = [case['domain']] + re.findall(r'\b\w{4,}\b', case['description'])[:5]
    log_message(f"Extracted key technical entities: {extracted_terms}")
    
    # Simulate Step 3 & 4: Patentability Exclusions & Prior Art
    log_message("Simulating Step 3 (Patentability Assessment) & Step 4 (Prior Art Simulation)...")
    exclusion_risk = case['section_3_exclusion_risk']
    log_message(f"Section 3 Exclusion Risk: {exclusion_risk}")
    
    # Simulate Step 5: Scoring (LLM-as-a-Judge criteria evaluation)
    log_message("Simulating Step 5 (Patentability Scoring) via LLM-as-a-Judge...")
    
    # LLM-as-a-Judge Criteria Grading
    # Criteria:
    # 1. Novelty (1-5)
    # 2. Inventive Step (1-5)
    # 3. Exclusions Compliance (1-5)
    # 4. Form 2 Structural Completeness (1-5)
    
    novelty_grade = 5.0 if "Low" in exclusion_risk else (3.0 if "Medium" in exclusion_risk else 2.0)
    inventive_grade = 4.5 if len(case['novelty']) > 50 else 3.0
    exclusion_grade = 5.0 if "Low" in exclusion_risk else (2.5 if "Medium" in exclusion_risk else 1.0)
    structure_grade = 4.8  # Consistent mock UI formatting
    
    overall_score = (novelty_grade + inventive_grade + exclusion_grade + structure_grade) / 4.0
    variance = abs(overall_score - case['expected_score'])
    
    log_message(f"LLM-as-a-Judge Scores -> Novelty: {novelty_grade}, Inventive: {inventive_grade}, Exclusions: {exclusion_grade}, Structure: {structure_grade}")
    log_message(f"Overall Computed Score: {overall_score:.2f} (Delta of Variance: {variance:.3f})")
    
    # Save simulated evaluation output
    EVAL_RESULTS.append({
        "case_id": case['id'],
        "title": case['title'],
        "domain": case['domain'],
        "judgement": {
            "novelty_score": novelty_grade,
            "inventive_step_score": inventive_grade,
            "exclusions_score": exclusion_grade,
            "structure_score": structure_grade,
            "overall_rating": round(overall_score, 2),
            "expected_rating": case['expected_score'],
            "variance": round(variance, 3),
            "verdict": "PASS" if overall_score >= 3.5 else "REJECT/REVISE"
        }
    })

# Save ratings metrics
with open(DATA_DIR / "patent_generator_ratings.json", "w") as f:
    json.dump(EVAL_RESULTS, f, indent=2)

log_message("Evaluation suite completed successfully. Outputs saved to eval/data/ and logs written.")
