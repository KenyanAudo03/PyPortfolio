import cv2
import numpy as np

def count_objects(image_path, min_area=500):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve accuracy
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use thresholding to create a binary image
    _, threshold = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Count the number of objects based on contour area
    object_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            object_count += 1
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('Counted Objects', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return object_count

# Replace 'your_image_path.jpg' with the actual path to your image
image_path = 'IMG_20240121_230256.jpg'
count = count_objects(image_path)
print(f'Number of objects: {count}')
