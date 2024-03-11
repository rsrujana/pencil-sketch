import cv2
import numpy as np

def pencil_sketch(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_gray, (81, 81), 0)
    inverted_blurred = 255 - blurred_image
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_sketch
