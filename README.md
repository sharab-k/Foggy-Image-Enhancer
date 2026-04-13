---
title: Foggy Image Enhancer
emoji: 🌫️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Foggy Image Enhancer & Object Detection Lab

This project demonstrates AI algorithms for enhancing road scene visibility under foggy conditions and analyzes their impact on YOLOv5 object detection performance.

## Pipeline
1. **Enhancement**: CLAHE, Gamma Correction, Bilateral Filtering, Dark Channel Prior.
2. **Detection**: YOLOv5 applied to enhanced images to compare accuracy.

## Deployment
- **Backend**: FastAPI (Docker on Hugging Face Spaces)
- **Frontend**: Vite + React (Vercel)
