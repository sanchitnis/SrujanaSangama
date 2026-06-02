# Grant Proposal: DST-SERB Core Research Grant (CRG)

## 1. Project Metadata
* **Project Title:** Non-Invasive, Privacy-Preserving Computer Vision Framework for Real-Time Student Engagement and Attention Analytics in Technical Education (Project: Srujana-Drishti)
* **Principal Investigator (PI):** HBK, Senior Faculty, School of Computing and Information Technology, REVA University
* **Co-Investigators (Co-PIs):**
  * Co-PI (Pedagogical Validation): Faculty, School of Education, REVA University
  * Co-PI (Cognitive Psychology): Faculty, Department of Psychology, School of Arts, Humanities, and Social Sciences, REVA University
* **Target Funding Scheme:** DST-SERB Core Research Grant (CRG)
* **Duration:** 3 Years (36 Months)
* **Broad Area:** Engineering Sciences
* **Sub-Area:** Computer Science & Information Technology (Computer Vision, Deep Learning, Learning Analytics)
* **Alignment:** Sustainable Development Goal 4 (Quality Education) & NEP 2020 (Multidisciplinary Research & Cognitive Engagement)
* **Total Estimated Budget:** ₹32,71,680 (Thirty-Two Lakhs Seventy-One Thousand Six Hundred and Eighty INR)

---

## 2. Executive Summary (Project Summary)
Modern technical education, especially in rigorous engineering disciplines, relies heavily on continuous cognitive engagement. Traditional classroom environments, however, lack a quantitative, objective, and real-time mechanism to gauge student attention and engagement levels. This research proposal introduces **Srujana-Drishti**, a non-invasive, privacy-preserving Computer Vision (CV) framework designed to assess cohort attention levels dynamically. Utilizing low-cost, standard classroom cameras, the system analyzes multi-modal physical cues—including head pose estimation, eye gaze tracking indices, micro-expression dynamics, and postural behaviors. 

Crucially, to address student privacy concerns, the framework adopts a "Privacy-by-Design" architecture. Face-related pre-processing occurs locally on decentralized edge-computing nodes (e.g., NVIDIA Jetson units) using localized geometric feature extraction. Raw video frames are permanently discarded immediately after processing, and only aggregated, anonymized engagement metrics are transmitted to a central visualization dashboard. The resulting real-time attention analytics will provide educators with instant, empirical feedback on their pedagogical effectiveness, mapping student attention spans during lecture timelines, and identifying struggling cohorts early. This multidisciplinary project bridges advanced AI, educational psychology, and instructional design to build a scalable model for next-generation smart classrooms.

---

## 3. Statement of Problem
Technical education requires active cognitive participation to master complex conceptual frameworks. Traditional teaching quality evaluations rely on retrospective, highly subjective student feedback surveys administered at the end of a semester. These surveys fail to provide actionable, real-time feedback that an instructor can use to modify delivery strategies mid-course. 

While commercial eye-tracking and facial analysis solutions exist, they suffer from two critical limitations:
1. **Infrastructure & Usability Bottlenecks:** They are designed for single-user desktop settings utilizing specialized hardware, making them cost-prohibitive and impractical for large-scale, high-density academic lecture halls.
2. **Severe Privacy Vulnerabilities:** Traditional cloud-based video analytics require streaming continuous raw classroom video feeds, raising significant ethical, legal, and privacy concerns regarding student surveillance.

There is a critical national gap for a scalable, cost-effective framework that can estimate multi-person, distant attention metrics in real-time, under varying illumination and posture occlusions, while strictly protecting the privacy of student identities.

---

## 4. Measurable Objectives & Quarterly Milestones

The project is structured into three primary annual objectives, divided into quarterly milestones:

*   **Objective 1 (Months 1–12): Development of Privacy-Preserving Edge Processing & Feature Extraction Models**
    *   *Q1:* Procurement of equipment and recruitment of the Junior Research Fellow (JRF).
    *   *Q2:* Development and optimization of MTCNN/RetinaFace models for high-density, multi-face detection under varying illumination.
    *   *Q3:* Development of an on-edge facial landmark coordinate extraction pipeline that immediately discards raw image matrices.
    *   *Q4:* Optimization of edge-deployment scripts on NVIDIA Jetson units, achieving a processing throughput of $\ge 15$ FPS for up to 60 students per classroom.

*   **Objective 2 (Months 13–24): Multi-Modal Fusion Engine & Classroom Attention Index (CAI) Formulation**
    *   *Q5:* Design of head-pose and eye-gaze estimation algorithms using geometry-based mathematical vectors rather than raw pixel data.
    *   *Q6:* Integration of postural analysis models (using skeletal coordinate mappings like MediaPipe Pose) to distinguish alert, slouched, or disengaged postures.
    *   *Q7:* Development of a Temporal Convolutional Network (TCN) to fuse head pose, gaze estimation, and postural metrics into a composite Classroom Attention Index (CAI) over sliding time windows.
    *   *Q8:* Development of an anonymized database structure to store temporal cohort-level attention data.

*   **Objective 3 (Months 25–36): Pilot Deployment, Interdisciplinary Validation, and Dashboard Integration**
    *   *Q9:* Construction of a real-time, cohort-level visual dashboard providing lecture-timeline attention metrics for instructors.
    *   *Q10:* Pilot installation of the hardware-software testbed in three high-density engineering lecture halls at REVA University.
    *   *Q11:* Interdisciplinary validation studies correlating CAI trends against objective student learning outcomes (concept quizzes, exams) and physiological load assessments.
    *   *Q12:* Final system optimization, report filing with DST-SERB, and submission of Scopus/WoS Q1 journal manuscripts.

---

## 5. Technical Methodology
The framework implements a decentralized, multi-layered pipeline to guarantee privacy while delivering highly accurate attention analytics.

```
[ Raw Classroom Video Stream ] (Low-cost IP cameras)
               │
               ▼
[ Layer 1: Edge Pre-Processing & Feature Extraction ]
  ├── Face Detection & Alignment (RetinaFace)
  ├── Landmark Coordinate Extraction (68-point mesh)
  └── *Raw Video Frame Purged (Local RAM only)*
               │
        [Landmark Vectors Only]
               │
               ▼
[ Layer 2: Multi-Modal Attention Engine (Local GPU/Server) ]
  ├── Gaze Tracking & Head Pose (ResNet-backed Estimator)
  ├── Postural Analysis (MediaPipe Pose Coordinate Mapping)
  └── Composite Classroom Attention Index (CAI) Fusion Model (TCN)
               │
       [CAI Score Timeline]
               │
               ▼
[ Layer 3: Analytics & Visualization Dashboard ]
  ├── Temporal Engagement Timelines for Faculty
  ├── Anonymized Cohort-Level Attention Heatmaps
  └── Early Warning Signals for At-Risk Classroom Blocks
```

### Layer 1: Edge Pre-Processing & Feature Extraction
*   **Edge Processing Node:** An NVIDIA Jetson developer kit is connected directly to standard classroom IP cameras. 
*   **Landmark Mesh Isolation:** A highly optimized face detector (RetinaFace) locates faces in the frame. A lightweight regression model extracts 68 facial landmark coordinates.
*   **Instant Purge:** The raw frame buffer is instantly cleared from the edge system's volatile memory (RAM). No raw images are written to disk or transmitted over the network. Only the structural coordinate matrices are passed to Layer 2.

### Layer 2: Multi-Modal Attention Engine
*   **Gaze Direction & Head Pose:** A spatial network estimates head yaw, pitch, and roll from the landmark coordinates. Gaze direction is estimated by mapping the geometric ratio between the iris center and eye corners.
*   **Postural Index:** MediaPipe Pose maps 33 skeletal keypoints of each student. Feature vectors representing posture state (e.g., leaning forward, upright, slouched, head resting on hand) are calculated.
*   **Temporal Fusion (TCN):** The coordinate sequences are fed into a Temporal Convolutional Network (TCN). The TCN fuses the multi-modal signals over sliding 30-second windows, outputting a continuous Classroom Attention Index (CAI) score between 0 (completely disengaged) and 100 (actively engaged).

### Layer 3: Analytics & Visualization Dashboard
*   **Faculty Feedback Panel:** Provides instructors with a post-lecture analytical chart showing the cohort's average engagement over the 50-minute timeline.
*   **Cohort Heatmaps:** Displays physical zones of the lecture hall where engagement consistently dips, enabling instructors to optimize classroom acoustics, visibility, and interaction patterns.

---

## 6. Interdisciplinary Validation & Co-PI Scope
To ensure the computer vision metrics map accurately to real cognitive states and educational outcomes, the project includes two specialized co-investigators:

1.  **Pedagogical Impact (School of Education Co-PI):**
    *   Integrates the CAI with established instructional frameworks (e.g., Bloom's Taxonomy, Active Learning).
    *   Coordinates classroom trials using different pedagogical structures (active learning segments vs. passive lectures) to evaluate how well the system detects behavioral transitions.
    *   Evaluates the usability and instructional value of the dashboard to faculty members.
2.  **Cognitive Load & Psychological Safety (Psychology Co-PI):**
    *   Grounds physical cues (micro-expressions, eye-blink frequencies) in cognitive psychology literature (such as Sweller’s Cognitive Load Theory).
    *   Conducts control experiments comparing CV attention metrics with gold-standard psychological attention tools (e.g., self-report questionnaires, selective attention tests).
    *   Establishes ethical guidelines and consent frameworks for student cohorts participating in the pilot classrooms.

---

## 7. Budget & Resource Estimates

### A. Non-Recurring (Capital Equipment)
| S.No | Equipment Description | Justification | Qty | Unit Cost (₹) | Total Cost (₹) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| 1 | GPU-Enabled Edge Computing Workstation | Required for model training, offline simulation, and localized fusion engine testing | 1 | 3,50,000 | 3,50,000 |
| 2 | NVIDIA Jetson Orin NX Developer Kits | For deployment as real-time processing edge nodes in pilot classrooms | 3 | 60,000 | 1,80,000 |
| 3 | High-Definition IP Cameras (PoE) | To capture wide-angle high-density cohort visual streams in 3 lecture halls | 6 | 15,000 | 90,000 |
| **A** | **Subtotal (Non-Recurring)** | | | | **6,20,000** |

### B. Recurring (Manpower & Consumables)
| S.No | Item | Justification | Year 1 (₹) | Year 2 (₹) | Year 3 (₹) | Subtotal (₹) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | **Manpower (Junior Research Fellow - JRF)** | NET/GATE qualified scholar to handle programming, model training, and integration (DST JRF Scale: ₹37,000/month + 24% HRA = ₹45,880/month) | 5,50,560 | 5,50,560 | 5,50,560 | 16,51,680 |
| 2 | **Consumables** | PoE network switches, local 12TB NAS storage server for anonymous vectors, high-speed cabling, cloud/GPU compute credits | 2,00,000 | 1,00,000 | 1,00,000 | 4,00,000 |
| 3 | **Travel** | Standard national conference travel (e.g., CVIP, IndiaIP), local field testing, visiting expert facilities (IISc/NIMHANS) | 50,000 | 50,000 | 50,000 | 1,50,000 |
| 4 | **Contingency** | Office supplies, software licenses, publication processing charges (APC) for high-impact Scopus journals | 1,00,000 | 25,000 | 25,000 | 1,50,000 |
| 5 | **Institutional Overheads** | As per standard SERB guidelines | 1,00,000 | 1,00,000 | 1,00,000 | 3,00,000 |
| **B** | **Subtotal (Recurring)** | | **10,00,560** | **8,25,560** | **8,25,560** | **26,51,680** |

### C. Total Project Cost (A + B): ₹32,71,680

---

## 8. Risk Analysis & Mitigation Plan

| Risk Description | Severity | Likelihood | Mitigation Strategy |
| :--- | :---: | :---: | :--- |
| **Privacy Concerns & Student Backlash:** Students or institutional boards objecting to video cameras in classrooms. | **High** | **Medium** | Edge architecture explicitly guarantees raw video is processed in volatile memory (RAM) and purged within milliseconds. Only coordinate meshes are saved. Student consent frameworks will be transparently managed by the Psychology Co-PI. |
| **High Density Occlusion:** Students blocking each other's faces or postures in a tiered lecture hall layout. | **Medium** | **High** | Dual-angle camera layout (two wide-angle cameras per hall) provides redundant fields of view. Posture and head-pose algorithms will fall back to landmark visibility confidence parameters. |
| **Compute Bottleneck on Edge:** Processing multiple streams at high resolutions in real-time exceeds Jetson capacity. | **Medium** | **Medium** | Landmark mesh extraction will use highly optimized, downscaled frames. Detection updates will run every 3rd frame, relying on correlation filters (optical flow tracking) in intermediate frames to maintain low compute overhead. |
