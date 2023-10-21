from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
# Open an image
image = Image.open("/content/Maserati.jpg")
# Convert the image to grayscale
image = image.convert("L")
# Apply the Sobel operators for gradient calculation
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
gradient_x = image.filter(ImageFilter.Kernel((3, 3), sobel_x))
gradient_y = image.filter(ImageFilter.Kernel((3, 3), sobel_y))
# Calculate the magnitude of the gradient
gradient_magnitude = np.sqrt(np.array(gradient_x)**2 +
np.array(gradient_y)**2)
# Display the original image and the gradient magnitude
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(132)
plt.imshow(gradient_x, cmap="gray")
plt.title("Sobel X Gradient")
plt.subplot(133)
plt.imshow(gradient_y, cmap="gray")
plt.title("Sobel Y Gradient")
plt.tight_layout()
plt.show()
plt.figure()
plt.imshow(gradient_magnitude, cmap="gray")
plt.title("Gradient Magnitude")
plt.show()