import cv2
import numpy as np
from ultralytics import YOLO

print("Loading YOLOv5 model from ultralytics...")
try:
    # This automatically downloads yolov5s if it doesn't exist
    model = YOLO('yolov5su.pt') 
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def detect_day_night(image):
    """
    Detects if the image is taken during day or night based on average brightness.
    Returns 'Day' or 'Night' and the average brightness value.
    """
    # Convert to LAB color space to get the L (Lightness) channel
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab[:, :, 0]
    avg_brightness = np.mean(l_channel)
    
    # Calculate percentage of dark pixels (below 90 lightness - handles glare better)
    dark_pixels_ratio = np.sum(l_channel < 90) / l_channel.size
    
    # A night image with headlights has high average brightness, 
    # but still contains a large percentage of relatively dark regions.
    if avg_brightness < 105: # Very dark overall
        status = "Night"
    elif dark_pixels_ratio > 0.4: # More than 40% is dark (sky, shadows)
        status = "Night"
    else:
        status = "Day"
        
    print(f"DEBUG: Brightness={avg_brightness:.2f}, DarkRatio={dark_pixels_ratio:.2f} -> {status}")
    return status, float(avg_brightness)

def detect_objects(image):
    """
    Run YOLOv5 object detection on a BGR image (OpenCV format).
    Returns the annotated image, the number of objects detected, and the average confidence.
    """
    if model is None:
        return image, 0, 0.0
        
    # YOLOv5 from Ultralytics can take BGR numpy arrays natively, 
    # but we pass RGB explicitly just to be safe
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Run inference (set verbose=False to keep logs clean)
    results = model(img_rgb, verbose=False)
    result = results[0]
    boxes = result.boxes
    
    num_objects = len(boxes)
    if num_objects > 0:
        avg_confidence = float(boxes.conf.mean().cpu().item())
    else:
        avg_confidence = 0.0
        
    # Draw bounding boxes on the ORIGINAL BGR image
    annotated_image = image.copy()
    
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
        conf = float(box.conf[0].cpu().item())
        cls_id = int(box.cls[0].cpu().item())
        name = result.names[cls_id]
        
        # Draw rectangle
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (229, 70, 79), 2)  # Indigo-ish color
        
        # Add label
        label = f"{name} {conf:.2f}"
        (label_width, label_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        
        # Background for text
        cv2.rectangle(annotated_image, (x1, y1 - label_height - baseline), (x1 + label_width, y1), (229, 70, 79), -1)
        cv2.putText(annotated_image, label, (x1, y1 - baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
    return annotated_image, num_objects, avg_confidence, None, None
