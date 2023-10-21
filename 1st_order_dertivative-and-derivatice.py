import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import cv2
# Load an image
image = cv2.imread("/content/Maserati.jpg", cv2.IMREAD_GRAYSCALE)
# Compute the first-order derivative along the x and y axes
dx = np.array([[-1, 0, 1]])
dy = dx.T
dx_derivative = convolve(image, dx)
dy_derivative = convolve(image, dy)
# Display the original image and its first-order derivatives
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(132)
plt.imshow(dx_derivative, cmap="gray")
plt.title("First-Order Derivative (X-axis)")
plt.subplot(133)
plt.imshow(dy_derivative, cmap="gray")
plt.title("First-Order Derivative (Y-axis)")
plt.tight_layout()
plt.show()