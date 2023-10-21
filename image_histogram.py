from PIL import Image
import matplotlib.pyplot as plt
image = Image.open("/content/Rotated-letter-7.png")
image = image.convert("L")
histogram = image.histogram()
plt.hist(histogram, bins=256, range=(0, 256), density=True,
color='gray', alpha=0.7)
plt.title("Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()