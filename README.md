---
title: Foggy Image Enhancer
emoji: 🌫️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Foggy Image Enhancer

This project is a web application designed to enhance images taken in foggy or hazy conditions. It uses advanced image processing techniques to improve visibility and clarity.

## Features
- Fog/Haze removal from images.
- Real-time enhancement using a backend API.
- Dockerized for easy deployment on Hugging Face Spaces.

## Setup and Deployment
This space is configured to run using Docker. The `Dockerfile` in the root directory handles the installation of dependencies and starts the backend server on port 7860.

### Local Development
To run the project locally:
1. Clone the repository.
2. Install dependencies listed in `backend/requirements.txt`.
3. Run `python backend/main.py`.
