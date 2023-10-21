from PIL import Image
import numpy as np
def histogram_equalization(image):
# Convert the image to grayscale
# Convert the image to a NumPy array
img_array = np.array(image)
# Calculate the histogram
hist, bins = np.histogram(img_array, bins=256, range=(0, 256))
# Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()
# Apply histogram equalization to the image
cdf_min = cdf.min()
img_eq = (cdf[img_array] - cdf_min) * 255 / (cdf[-1] - cdf_min)
# Convert the equalized NumPy array back to an image
equalized_image = Image.fromarray(np.uint8(img_eq))
return equalized_image
# Open an image
image = Image.open("/content/Screenshot 2023-10-16 192047.png")
# Perform histogram equalization
equalized_image = histogram_equalization(image)
# Display the original and equalized imag
equalized_image