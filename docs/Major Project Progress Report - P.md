# Major Project Progress Report - Phase 2 Review 1

**Academic Year:** 2025-2026  
**Semester:** 8th  
**Course Code:** —  
**School:** School of Computer Science and Engineering, B.Tech (CSIT), REVA University, Bengaluru, India

---

## Project Group Members Details

| Sl. No | SRN | Full Name | Sec | Mobile No. | Email ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | R21EJ001 | ABHINAV GOPAL P B | B | 7349711152 | 2108613@reva.edu.in |
| 2 | R21EJ007 | ARNAV GOPAL P | B | 9972366926 | 2108618@reva.edu.in |
| 3 | R21EJ134 | SANTOSH HJ | B | 7676393133 | 2101010@reva.edu.in |
| 4 | R22EJ092 | DISHANT DALAL | B | 9958702128 | 2210136704@reva.edu.in |

### Task Distribution
* **Project Leader:** ABHINAV GOPAL P
* **Documenter Lead:** SANTOSH H.J
* **Development Lead:** ARNAV GOPAL P, DISHANT DALAL

---

## Project Details

* **Project Title:** DEVELOP A FUNCTIONAL SOLUTION TO DEMONSTRATE THE FACE LIVELINESS DETECTION.
* **Type of Project:** Artificial Intelligence/Computer Vision Based Software application
* **Guide Details:** * **Name:** Harsha BK
  * **Designation:** Associate Professor
  * **Mobile No:** 8147883036
* **Place of Project Work:** School of CSE, REVA University
* **Remarks by Guide:** —
* **Date:** —

---

## Contents
1. [Project Implementation](#1-project-implementation)
   * 1.1. [Architectural Design](#11-architectural-design)
   * 1.2. [Class Diagram](#12-class-diagram)
   * 1.3. [Entity Relationship Model](#13-entity-relationship-model)
   * 1.4. [Sequence Diagram](#14-sequence-diagram)
   * 1.5. [Description of Technology Used](#15-description-of-technology-used)
2. [Conclusions](#2-conclusions)
3. [References](#3-references)

---

## 1. Project Implementation

The project implements a real-time face liveness detection system that determines whether the face presented to a camera belongs to a live person or is a spoof attempt (printed photo, video replay, or phone-screen display). 

The system runs entirely in a browser-based UI built with Streamlit and processes video from a standard USB webcam. All signal processing runs on CPU; no deep learning inference server or specialised hardware is required.

### Pipeline Steps (Per Video Frame)
* **Frame Capture:** OpenCV `VideoCapture` (`CAP_DSHOW` on Windows) reads frames at up to 30 FPS. Camera source is selectable from the UI dropdown.
* **Landmark Extraction:** MediaPipe `FaceMesh` extracts 468 facial landmarks plus iris landmarks (with `refine_landmarks=True`) per frame.
* **Six Parallel Signal Analyses:**
  1. **Blink Detection (EAR):** Eye Aspect Ratio calculation formula: 
     $$EAR = \frac{|p2-p6| + |p3-p5|}{2 \times |p1-p4|}$$
     A blink is counted when $EAR < 0.22$ for 2 consecutive frames.
  2. **Head Pose Detection:** Geometric ratio method comparing nose-to-forehead vs nose-to-chin detects UP/DOWN movements; nose horizontal offset detects LEFT/RIGHT movements. A 3-frame hysteresis prevents false triggers.
  3. **Texture Analysis (4 sub-signals):** Computes LBP entropy, FFT spike ratio, chromatic channel correlation, and specular highlight variance on a $64 \times 64$ face crop.
  4. **Optical Flow Micro-Motion:** Lucas-Kanade tracker deployed on 60 feature points. Live faces reflect $0.08 - 1.8 \text{ px/frame}$, while static photos record $\sim 0 \text{ px/frame}$.
  5. **Pupil Constriction Response:** Screen flashes every ~4 seconds; an iris radius change $\ge 6\%$ confirms a live eye.
  6. **Challenge-Response Engine:** Issues a randomized 2-step sequence drawn from `{BLINK, LOOK_LEFT, LOOK_RIGHT, LOOK_UP, LOOK_DOWN}`. The user must complete it within 20 seconds.
* **Confidence Scoring:** Fuses modules with the following weights: Challenge 40%, Texture 35%, Motion 15%, Pupil 10%. A **LIVE** verdict requires a total confidence score $\ge 0.55$, the challenge completed, AND a sustained texture score $> 0.36$.
* **Streamlit Web UI:** Features a dark-themed dashboard including a verdict card, countdown timer, challenge steps, per-signal breakdown bars, and a camera selector dropdown.

---

### 1.1 Architectural Design

The system is purely software-based and follows a layered pipeline architecture where each layer has a single, well-defined responsibility.

| Layer | Component | Responsibility |
| :--- | :--- | :--- |
| **Capture** | OpenCV VideoCapture | Reads webcam frames; applies `CAP_DSHOW` backend for Windows compatibility. |
| **Analysis** | MediaPipe + Detectors | Extracts 468 landmarks; runs blink, head pose, texture, motion, and pupil modules in parallel. |
| **Decision** | ConfidenceScorer + ChallengeEngine | Computes weighted confidence score, manages 20-second timer, issues LIVE/SPOOF/CHECKING verdict. |
| **Texture Gate** | Texture Analyzer | Hard gate: sustained texture score below 0.36 triggers SPOOF independently of challenge completion. |
| **UI** | Streamlit Dashboard | Displays live video feed, verdict card, countdown timer, signal breakdown bars, and challenge steps. |

#### Data Flow Pipeline:
$$\text{Webcam OpenCV VideoCapture} \longrightarrow \text{MediaPipe FaceMesh (468 + iris landmarks)}$$
$$\downarrow$$
$$\big[\text{BlinkDetector} \mid \text{Head Pose Detector} \mid \text{TextureAnalyzer} \mid \text{MotionAnalyzer} \mid \text{PupilResponseDetector}\big]$$
$$\downarrow$$
$$\text{ChallengeEngine} + \text{ConfidenceScorer} \longrightarrow \text{Verdict (LIVE / SPOOF / CHECKING)}$$
$$\downarrow$$
$$\text{Streamlit UI (verdict card, countdown timer, challenge steps, signal bars)}$$

---

### 1.2 Class Diagram

| Class | Key Attributes | Key Methods | Relation |
| :--- | :--- | :--- | :--- |
| **ConfidenceScorer** | `weights`, `live_threshold = 0.55`, `texture_fail_count`, `_history[]` | `update(ch, tx, mo, pu)`, `reset()` | Aggregates all 6 signal modules; produces final verdict |
| **BlinkDetector** | `EAR_THRESHOLD = 0.22`, `CONSEC_FRAMES = 2`, `blink_count` | `update(landmarks, w, h) -> dict` | Composed in pipeline; blink count feeds `ConfidenceScorer` |
| **HeadPoseDetector** | `_baseline_pitch`, `_pending_dir`, `_pending_count` | `update(landmarks, w, h) -> dict` | Geometric ratio method; composed in pipeline |
| **TextureAnalyzer** | `_history[]`, `live_threshold = 0.52` | `_lbp_entropy()`, `_fft_score()`, `_chromatic_score()`, `update(frame, bbox) -> dict` | 4 sub-signals; composed in pipeline |
| **MotionAnalyzer** | `_prev_gray`, `_prev_pts`, `MOTION_FLOOR = 0.08`, `MOTION_CEIL = 1.80` | `_init_tracker()`, `update(frame, bbox) -> dict` | Lucas-Kanade optical flow; composed in pipeline |
| **PupilResponseDetector** | `flash_active`, `response_detected`, `_pre_r[]`, `_post_r[]` | `update(landmarks, w, h) -> dict` | Flash-triggered iris radius; composed in pipeline |
| **ChallengeEngine** | `num_steps = 2`, `steps[]`, `_blink_base` | `generate()`, `update(blink_r, head_r) -> dict` | Randomised ordered challenge sequence; composed in pipeline |
| **Camera** | `source`, `width`, `height` | `open()`, `read()`, `read_rgb()`, `release()` | OpenCV `VideoCapture` wrapper; context-manager support |

---

### 1.3 Entity Relationship Model

* **SESSION:** `session_id` (PK), `start_timestamp`, `end_timestamp`, `final_verdict`, `final_confidence`, `timed_out`, `timeout_seconds`
* **FRAME:** `frame_id` (PK), `session_id` (FK), `timestamp`, `fps`, `face_detected`, `face_bbox_x1`, `face_bbox_y1`, `face_bbox_x2`, `face_bbox_y2`
* **CHALLENGE:** `challenge_id` (PK), `session_id` (FK), `challenge_type` (BLINK/LOOK_LEFT/LOOK_DOWN/LOOK_RIGHT/LOOK_UP), `sequence_order`, `is_completed`, `completion_timestamp`
* **BLINK_EVENT:** `blink_id` (PK), `frame_id` (FK), `ear_left`, `ear_right`, `ear_avg`
* **HEAD_MOVEMENT:** `movement_id` (PK), `frame_id` (FK), `yaw`, `pitch`, `direction` (L/R/U/D/CENTER)
* **TEXTURE_RESULT:** `texture_id` (PK), `frame_id` (FK), `lbp_score`, `fft_score`, `chrom_score`, `spec_score`, `composite_score`

#### Key Relationships:
* **SESSION** $\longrightarrow$ **FRAME** ($1:N$)
* **SESSION** $\longrightarrow$ **CHALLENGE** ($1:N$)
* **FRAME** $\longrightarrow$ **BLINK_EVENT** ($1:0..1$)
* **FRAME** $\longrightarrow$ **HEAD_MOVEMENT** ($1:0..1$)
* **FRAME** $\longrightarrow$ **TEXTURE_RESULT** ($1:0..1$ - computed every frame)

---

### 1.4 Sequence Diagram
**Use Case:** User completes a liveness verification session.

| # | From | To | Event |
| :--- | :--- | :--- | :--- |
| 1 | User | Streamlit UI | Clicks "Start Detection" |
| 2 | Streamlit UI | ChallengeEngine | Generates random 2-step challenge sequence |
| 3 | Streamlit UI | OpenCV VideoCapture | `VideoCapture.open()` with `CAP_DSHOW` backend |
| 4 | Webcam | OpenCV | Returns BGR frame at up to 30 FPS |
| 5 | OpenCV | MediaPipe FaceMesh | `process(RGB frame)` |
| 6 | MediaPipe FaceMesh | Pipeline | Returns 468 + iris landmarks |
| 7 | Pipeline | BlinkDetector | `update(landmarks, w, h)` $\rightarrow$ `blink_result` |
| 8 | Pipeline | HeadPoseDetector | `update(landmarks, w, h)` $\rightarrow$ `direction` |
| 9 | Pipeline | TextureAnalyzer | `update(frame, bbox)` $\rightarrow$ `texture_result` |
| 10 | Pipeline | MotionAnalyzer | `update(frame, bbox)` $\rightarrow$ `motion_result` |
| 11 | Pipeline | PupilResponseDetector | `update(landmarks, w, h)` $\rightarrow$ `pupil_result` |
| 12 | Pipeline | ChallengeEngine | `update(blink_r, head_r)` $\rightarrow$ `challenge_result` |
| 13 | Pipeline | ConfidenceScorer | `update(ch, tx, mo, pu)` $\rightarrow$ `verdict`, `confidence` |
| 14 | ConfidenceScorer | ConfidenceScorer | Check: `elapsed > 20s` $\rightarrow$ **SPOOF (timeout)** |
| 15 | ConfidenceScorer | ConfidenceScorer | Check: `texture_fail_count > 20` $\rightarrow$ **SPOOF (texture gate)** |
| 16 | ConfidenceScorer | ConfidenceScorer | Check: `confidence >= 0.55 AND all_done` $\rightarrow$ **LIVE** |
| 17 | Streamlit UI | Streamlit UI | Updates verdict card, timer, challenge steps, signal bars |
| 18 | *[Timeout]* | — | SPOOF displayed; session awaits START/NEW |
| 19 | *[Success]* | — | All challenges done + confidence threshold met $\rightarrow$ **LIVE** |

---

### 1.5 Description of Technology Used

| Technology | Version | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.11 | Core programming language for all modules. |
| **Streamlit** | $\ge 1.35$ | Browser-based UI: camera selector, verdict card, signal breakdown bars, CSS injection. |
| **OpenCV** | $\ge 4.9.0$ | Webcam capture via `CAP_DSHOW`, image processing, optical flow, JPEG encoding. |
| **MediaPipe** | 0.10.9 | FaceMesh: 468 3D facial landmarks plus 10 iris landmarks per frame in real time. |
| **NumPy** | $\ge 1.24$ | Array operations on landmark coordinates, LBP computation, and FFT analysis. |
| **SciPy** | $\ge 1.11$ | Euclidean distance for Eye Aspect Ratio via `scipy.spatial.distance`. |
| **imutils** | 0.5.4 | Frame resize utilities and convenience wrappers for OpenCV operations. |
| **Pillow** | $\ge 9.0$ | Image I/O helpers for frame format conversion. |
| **USB Webcam (UVC)** | — | Hardware input; both built-in and external USB webcams supported via camera selector UI. |

---

## 2. Conclusions

The following milestones have been implemented and verified in Phase 2:
* **6-Signal Liveness Pipeline:** A functional evaluation structure combining blink detection (EAR), head pose estimation via geometric landmark ratios, texture analysis (LBP, FFT, chromatic noise, and specular variance), Lucas-Kanade optical flow micro-motion, and pupil constriction response—all optimized entirely for execution on a standard CPU in real time.
* **Randomized Challenge Engine:** An ordered challenge-response generator that provides a unique 2-step action sequence per session chosen from `{BLINK, LOOK_LEFT, LOOK_RIGHT, LOOK_UP, LOOK_DOWN}`. This layout makes pre-recorded video replay attacks completely ineffective.
* **Hard Timeout Enforcement:** A built-in 20-second countdown timer that automatically marks the current tracking session as `SPOOF` if the user fails to execute every step within the designated timeframe.
* **Texture Hard Gate:** A security feature that triggers an absolute `SPOOF` verdict if the composite texture score remains below 0.36 for more than 20 consecutive frames, specifically designed to mitigate physical photo attacks where a printed portrait is manually manipulated or tilted.
* **Fused Scoring Model:** A mathematical weighted framework blending all modules (Challenge 40%, Texture 35%, Motion 15%, Pupil 10%), defining a strict condition threshold of a cumulative confidence score $\ge 0.55$ to yield a final **LIVE** status.
* **Interactive Dashboard:** A dark-themed Streamlit visual client configured with a hardware camera selection list, structural landmark overlays, live scoring indicator bars, and an urgency-colored clock shifting dynamically from green to orange and finally to red.
* **Stand-Alone Optimization:** The system successfully achieves real-time liveness processing without requiring deep learning inference backends or dedicated hardware acceleration setups.

---

## 3. References

* **[1]** T. Soukupová and J. Čech, "Real-time eye blink detection using facial landmarks," in *Proc. 21st Computer Vision Winter Workshop (CVWW)*, Feb. 2016, pp. 1-8.
* **[2]** T. Ojala, M. Pietikainen, and T. Maenpaa, "Multiresolution gray-scale and rotation invariant texture classification with local binary patterns," *IEEE Trans. Pattern Anal. Mach. Intell.*, vol. 24, no. 7, pp. 971-987, Jul. 2002.
* **[3]** Z. Boulkenafet, J. Komulainen, and A. Hadid, "Face spoofing detection using colour texture analysis," *IEEE Trans. Inf. Forensics Security*, vol. 11, no. 8, pp. 1818-1830, Aug. 2016.
* **[4]** B. D. Lucas and T. Kanade, "An iterative image registration technique with an application to stereo vision," in *Proc. 7th Int. Joint Conf. Artificial Intelligence (IJCAI)*, 1981, pp. 674-679.
* **[5]** Google LLC, "MediaPipe Face Mesh," 2023. [Online]. Available: [https://google.github.io/mediapipe/solutions/face_mesh](https://google.github.io/mediapipe/solutions/face_mesh)
* **[6]** G. Bradski, "The OpenCV Library," *Dr. Dobb's Journal of Software Tools*, 2000. [Online]. Available: [https://docs.opencv.org/4.9.0/](https://docs.opencv.org/4.9.0/)
* **[7]** Streamlit Inc., "Streamlit Documentation v1.35," 2024. [Online]. Available: [https://docs.streamlit.io](https://docs.streamlit.io)
"""
