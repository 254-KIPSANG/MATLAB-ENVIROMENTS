# -*- coding: utf-8 -*-
"""Image Filtering.ipynb


import cv2
import numpy as np

# Define the input image as a numpy array
input_image = np.array([
    [89, 81, 35, 38, 57, 17, 23, 11],
    [96, 24, 83, 57, 47, 60, 91, 96],
    [55, 93, 59, 8, 1, 26, 15, 10],
    [14, 35, 55, 5, 34, 65, 83, 77],
    [15, 20, 92, 53, 16, 69, 54, 82],
    [26, 25, 29, 78, 79, 75, 100, 87],
    [84, 62, 76, 93, 31, 45, 8, 8],
    [25, 47, 75, 13, 53, 8, 44, 40]
], dtype=np.uint8)

# Define the filters
mask_1 = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]
], dtype=np.float32)
mask_2 = np.ones((3, 3), dtype=np.float32) / 9
mask_3 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)
mask_4 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply each filter to the input image using OpenCV's filter2D function
filter_image_1 = cv2.filter2D(input_image, -1, mask_1)  # Edge Filter
filter_image_2 = cv2.filter2D(input_image, -1, mask_2)  # Averaging Filter
filter_image_3 = cv2.filter2D(input_image, -1, mask_3)  # Sharpen Filter
filter_image_4 = cv2.filter2D(input_image, -1, mask_4)  # Custom Filter

# Display the output matrices of each filter operation
print("Filter Image 1 (Edge Filter):\n", filter_image_1)
print("\nFilter Image 2 (Averaging Filter):\n", filter_image_2)
print("\nFilter Image 3 (Sharpen Filter):\n", filter_image_3)
print("\nFilter Image 4:\n", filter_image_4)