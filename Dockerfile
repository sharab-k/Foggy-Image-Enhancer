# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the backend requirements first for caching
COPY backend/requirements.txt ./backend/

# Install dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the backend code
COPY backend/ ./backend/

# Hugging Face Spaces run on port 7860 by default
ENV PORT=7860
EXPOSE 7860

# Run from the backend directory
WORKDIR /app/backend
CMD ["python", "main.py"]
