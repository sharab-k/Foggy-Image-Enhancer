CS4092  
Final Year Project  
**Foggy Image Enhancer**

Submitted By  

| Student Name | Roll Number |
| :--- | :--- |
| Noman Ahmed Siddiqui | 22K-4252 |
| Ansh Kumar | 22K-4564 |
| Affan Jan | 22K-4475 |

**Project Progress Report**  
Department of Computer Science  
National University of Computer and Emerging Sciences  
FAST – Karachi Campus

### 1 INTRODUCTION

This project explores an AI-powered computer vision platform designed to overcome the challenge of object detection in poor visibility. Specifically, it focuses on enhancing road scene visibility under foggy conditions and analyzes how these enhancements impact YOLOv5 object detection performance. The system allows users to upload blurry or foggy images, automatically applies enhancement algorithms, and then runs real-time object detection natively on both the original and enhanced images for comparative analysis.

The image enhancement pipeline seamlessly integrates techniques such as Contrast Limited Adaptive Histogram Equalization (CLAHE), Gamma Correction, Bilateral Filtering, and Dark Channel Prior (DCP) to restore visibility. The YOLOv5 object detection model then evaluates the processed outputs against the originals to demonstrate empirical improvements in accuracy and bounding box confidence scores. During FYP Part 1, the core image enhancement algorithms were developed, object detection models were benchmarked, and the initial backend API was built. FYP Part 2 focuses heavily on developing an interactive React frontend, containerizing the application using Docker, optimizing the heavy computer vision operations for resource-constrained free-tier cloud environments (Hugging Face Spaces and Vercel), and resolving cross-origin deployment errors.

### 2 TIMELINE

The following timeline was established during FYP Part 1 and covers the work completed in that phase.

**FYP Part 1 Timeline (Completed)**

| Period | Activities |
| :--- | :--- |
| Weeks 1–3 | Requirements gathering, literature review on dehazing algorithms, and system architecture design |
| Weeks 4–6 | Implementation of core enhancement techniques (CLAHE, Gamma Correction, Bilateral Filtering, DCP) |
| Weeks 7–9 | YOLOv5 object detection setup and baseline comparison evaluation on foggy datasets |
| Weeks 10–12 | Backend development using FastAPI and encapsulation of the processing logic |
| Weeks 13–15 | Pipeline testing and analysis of enhancement effects on object detection confidence scores |

### 3 PROGRESS

FYP Part 2 began after the completion of the core computer vision algorithms and baseline application structure in FYP Part 1. The following subsections describe the work completed so far in FYP Part 2, leading up to the mid-evaluation.

#### 3.1 FRONTEND DEVELOPMENT AND INTEGRATION

To provide an interactive platform for the models, a dynamic frontend interface was developed during FYP Part 2 using Vite and React. The application features a robust drag-and-drop file upload mechanism, enabling users to seamlessly upload their test images. The interface provides a side-by-side comparison view allowing direct visual analysis of the original image against the algorithmically enhanced image. Furthermore, it overlays YOLOv5 bounding boxes and confidence score labels to visually demonstrate the object detection pipeline’s outputs. All data transfers were optimized via REST API routes using efficient multipart form-data handling for processing image streams between the React frontend and FastAPI backend.

#### 3.2 DEPLOYMENT AND CLOUD OPTIMIZATION

A substantial part of FYP Part 2 was dedicated to transitioning the project from a local development codebase to a fully deployed cloud infrastructure. Docker containerization was set up for the FastAPI backend to seamlessly host the inference models on Hugging Face Spaces. The React frontend was successfully deployed to Vercel. A significant challenge faced and resolved was optimizing the resource-heavy computer vision pipeline to execute reliably within the strict memory and compute limitations of Hugging Face’s free tier. Additionally, widespread Cross-Origin Resource Sharing (CORS) setup issues and module path errors were mitigated to guarantee stable and uninterrupted bidirectional communication between the Vercel frontend and Hugging Face backend.

**FYP Part 2 – Work Completed (Before Mid Evaluation)**

| Task | Description | Status |
| :--- | :--- | :--- |
| Frontend Development | Built Vite/React interface with side-by-side visual comparison view | Completed |
| Backend Integration | Unified frontend and FastAPI backend APIs for image streaming | Completed |
| Cloud Containerization | Created Docker configuration for seamless backend deployment | Completed |
| Pipeline Optimization | Optimized YOLOv5 inferences to operate within Hugging Face free-tier constraints | Completed |
| CORS and Deployment | Resolved cross-origin and Vercel build errors; achieved full deployment | Completed |

**Remaining Milestones (After Mid Evaluation – 1 Month)**

The following three milestones are planned for the remaining one month of FYP Part 2, from mid evaluation to the final submission.

| # | Milestone | Timeline | Status |
| :--- | :--- | :--- | :--- |
| 1 | Advanced Analytics Metrics Comparison | Weeks 1–2 | Planned |
| 2 | End-to-End Latency Improvements | Week 3 | Planned |
| 3 | System Testing and Documentation | Weeks 3–4 | Planned |

Milestone 1 involves generating analytical metrics within the React frontend, automatically comparing detection confidence percentages before and after enhancements.  
Milestone 2 addresses end-to-end latency optimizations such as payload compression and response buffering to ensure the YOLOv5 and DCP algorithms remain responsive.  
Milestone 3 covers final validation, load testing of the cloud endpoints, bug fixing, and developing the final project documentation and manuals.

### 4 UPDATED TIMELINE

The following updated timeline covers the entire project from proposal to completion, spanning both FYP Part 1 and FYP Part 2.

| Phase | Period | Activities |
| :--- | :--- | :--- |
| FYP 1 | Weeks 1–3 | Requirements, architecture, literature review, and algorithm design |
| FYP 1 | Weeks 4–6 | Implementation of enhancement algorithms (CLAHE, DCP, Gamma, etc.) |
| FYP 1 | Weeks 7–9 | YOLOv5 integration and baseline image fog evaluations |
| FYP 1 | Weeks 10–12 | Backend FastAPI development and container logic mock-up |
| FYP 1 | Weeks 13–15 | Pipeline design and initial qualitative testing |
| FYP 2 | Weeks 1–3 | Frontend development (Vite + React framework, layout design) (Completed) |
| FYP 2 | Weeks 4–6 | Frontend & Backend integration, REST endpoint stability (Completed) |
| FYP 2 | Weeks 7–8 | Dockerize backend, Hugging Face deployment, optimization (Completed) |
| FYP 2 | Weeks 9–10 | Advanced analytics metric integration UI (Planned) |
| FYP 2 | Week 11 | End-to-End inference latency improvements (Planned) |
| FYP 2 | Weeks 11–12 | Stress testing, code refactor, and final reporting (Planned) |

### REFERENCES

[1] K. He, J. Sun, and X. Tang, “Single Image Haze Removal Using Dark Channel Prior,” IEEE Transactions on Pattern Analysis and Machine Intelligence, 2011.  
[2] J. Redmon et al., “You Only Look Once: Unified, Real-Time Object Detection,” arXiv, 2015.  
[3] Ultralytics, “YOLOv5 Documentation,” 2020.  
[4] FastAPI Documentation, https://fastapi.tiangolo.com.  
[5] Hugging Face Documentation, https://huggingface.co/docs.  
[6] Vite Documentation, https://vitejs.dev/guide/.  
[7] Docker Documentation, https://docs.docker.com.
