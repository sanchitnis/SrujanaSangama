# Grant Proposal Outline: DST-SERB Core Research Grant (CRG)

## 1. Project Metadata
* **Project Title:** Non-Invasive, Privacy-Preserving Computer Vision Framework for Real-Time Student Engagement and Attention Analytics in Technical Education (Project: Srujana-Drishti)
* **Principal Investigator (PI):** HBK, Senior Faculty, School of Computing and Information Technology, REVA University
* **Target Funding Scheme:** DST-SERB Core Research Grant (CRG)
* **Duration:** 3 Years (36 Months)
* **Broad Area:** Engineering Sciences
* **Sub-Area:** Computer Science & Information Technology (Computer Vision, Deep Learning, Learning Analytics)
* **Alignment:** Sustainable Development Goal 4 (Quality Education)

---

## 2. Executive Summary (Project Summary)
Modern technical education, especially in engineering disciplines, requires active student cognitive engagement. However, traditional classrooms lack a quantitative, real-time mechanism to measure student attention and engagement levels. This project proposes **Srujana-Drishti**, a non-invasive, privacy-preserving Computer Vision (CV) framework designed to assess student attention dynamically. 

By utilizing standard classroom cameras, the system will analyze multi-modal physical cues—including head pose estimation, gaze tracking indices, micro-expression dynamics, and postural behaviors. To address privacy concerns, all face-related processing will happen on edge computing nodes using localized feature extraction, immediately discarding raw video frames and storing only aggregated, anonymized engagement metrics. The resulting attention analytics will provide instructors with actionable feedback on pedagogical effectiveness and help identify struggling students early.

---

## 3. Measurable Objectives
1. **Objective 1 (Months 1–12):** Design and train light-weight, privacy-preserving deep learning models optimized for edge deployment to perform real-time head-pose estimation and gaze-direction tracking in high-density classroom environments.
2. **Objective 2 (Months 13–24):** Develop a multi-modal fusion algorithm that combines facial landmark dynamics, micro-expressions, and body posture to generate a composite "Classroom Attention Index" (CAI).
3. **Objective 3 (Months 25–36):** Deploy a pilot testbed in three engineering lecture halls at REVA University, validating the framework's reliability, computing overhead, and pedagogical impact over a full academic semester.

---

## 4. Novelty & Scientific Significance
* **Privacy-by-Design Edge Architecture:** Unlike cloud-based systems that upload raw feeds, this framework extracts abstract geometric facial/posture features locally on edge nodes. Raw video is discarded instantly, protecting student identities.
* **High-Density Multi-Person Analytics:** Current gaze-tracking methods are designed for single users in front of a monitor. This project addresses the challenge of multi-person, distant gaze estimation in structured classrooms with varying illumination and occlusions.
* **Pedagogical Feedback Integration:** Rather than just tracking individuals, the system aggregates data to provide teachers with a timeline of lecture engagement (e.g., indicating that attention dropped significantly during minutes 20–25), enabling empirical optimization of teaching methods.

---

## 5. Technical Methodology
The framework comprises three primary architectural layers:

```
[ Classroom Video Stream ]
           │
           ▼
[ Layer 1: Edge Pre-Processing & Feature Extraction ]
  ├── Face Detection & Alignment (MTCNN/RetinaFace)
  ├── Landmark Extraction & Anonymization
  └── *Raw Video Discarded*
           │
           ▼
[ Layer 2: Multi-Modal Attention Engine ]
  ├── Gaze Tracking & Head Pose (ResNet-backed Estimator)
  ├── Postural Analysis (MediaPipe Pose / OpenPose)
  └── Composite Classroom Attention Index (CAI) Model
           │
           ▼
[ Layer 3: Analytics & Visualization Dashboard ]
  ├── Temporal Engagement Timelines for Faculty
  ├── Anonymized Cohort-Level Attention Heatmaps
  └── Early Warning Signals for At-Risk Students
```

1. **Detection & Feature Extraction (Edge):** Input streams from low-cost classroom cameras are processed on edge units (e.g., NVIDIA Jetson). Faces are detected and represented solely as coordinate vectors of facial landmark points.
2. **Attention Synthesis:** 
   * **Gaze Index:** Calculated based on head yaw/pitch and eye aspect ratios (EAR) to determine focus toward the board/instructor.
   * **Postural Index:** Evaluates body alignment (leaning forward vs. slouched back) to infer active vs. passive states.
3. **Synthesis Engine:** A Temporal Convolutional Network (TCN) integrates these inputs over time windows to compute the attention index.

---

## 6. Budget & Resource Estimates (Target: ~35–45 Lakhs INR)
* **Equipment (Capital):** GPU-enabled Edge computing workstation, NVIDIA Jetson developer kits, high-definition IP cameras for pilot classrooms.
* **Manpower (Recurring):** 1 Junior Research Fellow (JRF) / Project Associate for 36 months (DST guidelines).
* **Consumables:** Networking hardware, data storage, computing resources.
* **Travel & Contingency:** Domain expert consultations, field testing, conference presentations.
* **Overheads:** As per REVA University institutional rules.
