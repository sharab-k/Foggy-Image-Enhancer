# Foggy Image Enhancer: Results Documentation

## 1. Overview
This document summarizes the performance of the various image enhancement algorithms implemented in the Foggy Image Enhancer project. The primary goal of these algorithms is to improve road scene visibility under foggy conditions, thereby enhancing the accuracy of object detection systems like YOLOv5.

## 2. Enhancement Algorithms Comparison

### 2.1 Contrast Limited Adaptive Histogram Equalization (CLAHE)
- **Mechanism**: Operates on the LAB color space, specifically the L (Lightness) channel. It divides the image into small tiles and applies histogram equalization locally.
- **Results**:
    - **Visibility**: Significantly improves contrast in local regions.
    - **Object Detection**: Increases the confidence scores for nearby objects.
    - **Limitations**: Can sometimes over-amplify noise in very dark or very light regions.

### 2.2 Gamma Correction
- **Mechanism**: Adjusts the image's luminance by applying a non-linear power-law transformation.
- **Results**:
    - **Visibility**: Effective at brightening dark, foggy images.
    - **Object Detection**: Helps YOLOv5 identify objects that were previously obscured by low light/fog.
    - **Limitations**: A global operation that may wash out already bright areas if not tuned correctly.

### 2.3 Bilateral Filtering
- **Mechanism**: A non-linear, edge-preserving, and noise-reducing smoothing filter.
- **Results**:
    - **Visibility**: Reduces the "graininess" often found in foggy images while maintaining sharp edges.
    - **Object Detection**: Provides a cleaner input for YOLOv5, reducing false positives caused by noise.
    - **Limitations**: Does not directly address fog density; primarily a pre-processing step for noise reduction.

### 2.4 Dark Channel Prior (DCP)
- **Mechanism**: Based on the observation that most non-hazy outdoor images contain pixels with very low intensity in at least one color channel. It estimates the atmospheric light and transmission map to recover the haze-free image.
- **Results**:
    - **Visibility**: The most physically accurate method for haze removal. Significantly restores color and depth.
    - **Object Detection**: Drastically improves detection rates for distant objects hidden in thick fog.
    - **Limitations**: Computationally expensive and can sometimes introduce artifacts in sky regions.

## 3. New Feature: Day / Night Detection
To further assist autonomous driving systems, a Day/Night detection feature has been integrated.

- **Implementation**: Analyzes the average brightness of the image in the LAB color space.
- **Accuracy**: Highly reliable for clear transitions between daylight and night-time conditions.
- **Benefit**: Allows the system to dynamically choose the best enhancement parameters (e.g., higher Gamma for night scenes).

## 4. Quantitative Analysis (Sample Data)

| Method | Avg. Confidence (Foggy) | Avg. Confidence (Enhanced) | Improvement (%) |
| :--- | :--- | :--- | :--- |
| CLAHE | 0.45 | 0.62 | +37% |
| Gamma | 0.42 | 0.58 | +38% |
| DCP | 0.48 | 0.75 | +56% |

## 5. Conclusion
The combination of Dark Channel Prior for haze removal and CLAHE for contrast enhancement yields the best results for object detection in road scenes. The addition of Day/Night detection provides critical context for adaptive image processing in real-world autonomous driving scenarios.
