import cv2
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply edge detection
    edges = cv2.Canny(image, 50, 150)
    
    # Detect lines (e.g., walls) using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
    
    structure_data = []  # Store wall, door, and window data
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            structure_data.append({"type": "wall", "coords": (x1, y1, x2, y2)})
    
    print("Extracted structure data:", structure_data)
    return structure_data
