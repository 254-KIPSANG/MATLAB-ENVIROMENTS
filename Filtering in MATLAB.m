% Close all open figures, clear workspace, and clear command window
close all;
clear all;
clc;

% Define the input image as a matrix
InputImage = [
    89, 81, 35, 38, 57, 17, 23, 11;
    96, 24, 83, 57, 47, 60, 91, 96;
    55, 93, 59, 8, 1, 26, 15, 10;
    14, 35, 55, 5, 34, 65, 83, 77;
    15, 20, 92, 53, 16, 69, 54, 82;
    26, 25, 29, 78, 79, 75, 100, 87;
    84, 62, 76, 93, 31, 45, 8, 8;
    25, 47, 75, 13, 53, 8, 44, 40;
];

% Define the masks for different filters
Mask_1 = [
    1, 1, 1;
    0, 0, 0;
    -1, -1, -1
];
Mask_2 = [
    1, 1, 1;
    1, 1, 1;
    1, 1, 1
];
Mask_3 = [
    0, -1, 0;
    -1, 5, -1;
    0, -1, 0
];
Mask_4 = [
    -1, -1, -1;
    -1, 8, -1;
    -1, -1, -1
];

% Apply each filter to the input image using 'imfilter' function
FilterImage_1 = imfilter(InputImage, Mask_1); % Edge Filter
FilterImage_2 = imfilter(InputImage, (1/9)*Mask_2); % Averaging Filter
FilterImage_3 = imfilter(InputImage, Mask_3); % Sharpen Filter
FilterImage_4 = imfilter(InputImage, Mask_4); % Filter

% Display the output matrices of each filter operation
disp('Filter Image 1 (Edge Filter):');
disp(FilterImage_1);

disp('Filter Image 2 (Averaging Filter):');
disp(FilterImage_2);

disp('Filter Image 3 (Sharpen Filter):');
disp(FilterImage_3);

disp('Filter Image 4:');
disp(FilterImage_4);
