from PIL import Image, ImageFilter
# Open an image
image = Image.open("/content/Screenshot 2023-10-16 192047.png")
# Apply Gaussian smoothing to the image
smoothed_image = image.filter(ImageFilter.GaussianBlur(radius=2))
# Display the original and smoothed images
image.show(title="Original Image")
smoothed_image.show(title="Smoothed Image")
plt.show(smoothed_image)