# MATLAB-ENVIROMENTS
ONLY MATLAB STUFFS HERE
# Image Filtering in MATLAB

## Introduction
This MATLAB script demonstrates basic image filtering techniques using the `imfilter` function. Image filtering is a fundamental operation in image processing used to enhance or manipulate images by applying mathematical operations to each pixel or neighborhood of pixels in an image.

## Description
- The script first defines an input image as a matrix. In this example, the input image is a grayscale image represented as a matrix of pixel intensity values.
- Four different filters are defined as matrices (`Mask_1`, `Mask_2`, `Mask_3`, and `Mask_4`). Each filter matrix represents a specific convolution kernel used for different filtering operations.
- The `imfilter` function is then used to apply each filter to the input image separately, resulting in four filtered images: `FilterImage_1`, `FilterImage_2`, `FilterImage_3`, and `FilterImage_4`.
- Each filtered image is displayed using the `disp` function to showcase the effect of different filtering operations on the input image.

## Filters Used
1. **Edge Filter (Mask_1):** Detects edges in the image by emphasizing abrupt intensity changes.
2. **Averaging Filter (Mask_2):** Blurs the image by replacing each pixel's value with the average value of its neighboring pixels.
3. **Sharpen Filter (Mask_3):** Enhances the edges in the image by emphasizing the high-frequency components.
4. **Custom Filter (Mask_4):** A custom filter designed to demonstrate the flexibility of image filtering operations.

## Usage
- Ensure that MATLAB is installed on your system.
- Copy the provided script into a MATLAB editor or script file.
- Run the script to observe the filtered images displayed in the MATLAB command window.

## License
This script is provided under the MIT License. Feel free to modify and use it according to your requirements.

