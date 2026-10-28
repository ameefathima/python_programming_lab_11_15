# Program to Perform Image Processing Operations Using NumPy

import numpy as np

image = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [90, 100, 110, 120],
                  [130, 140, 150, 160]])

print("Original Image:")
print(image)

# Reshape the image
reshaped = image.reshape(2, 8)

# Extract a specific region
region = image[0:2, 0:2]

# Increase brightness using broadcasting
bright = np.clip(image + 50, 0, 255)

# Create a transformation matrix
transform = np.array([[1, 0],
                      [0, 1]])

# Perform matrix multiplication
result = np.dot(region, transform)

print("\nReshaped Image:")
print(reshaped)

print("\nSelected Region:")
print(region)

print("\nBrightness Adjusted Image:")
print(bright)

print("\nTransformed Region:")
print(result)