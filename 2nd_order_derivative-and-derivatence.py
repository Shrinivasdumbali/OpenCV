import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import cv2
# Load an image
image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)
# Compute the second-order derivative along the x and y axes
d2x = np.array([[1, -2, 1]])
d2y = d2x.T
d2x_derivative = convolve(image, d2x)
d2y_derivative = convolve(image, d2y)
# Display the original image and its second-order derivatives
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(132)
plt.imshow(d2x_derivative, cmap="gray")
plt.title("Second-Order Derivative (X-axis)")
plt.subplot(133)
plt.imshow(d2y_derivative, cmap="gray")
plt.title("Second-Order Derivative (Y-axis)")
plt.tight_layout()
plt.show()