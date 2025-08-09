from PIL import Image  # Library to work with images

img = Image.open(r"test.bmp")  # Open the original image

width, height = img.size  # Get image dimensions

pixels = img.load()  # Access the pixels for editing
# Make the top-left quarter of the image black
for x in range(width // 2):
    for y in range(height // 2):
        pixels[x, y] = (0, 0, 0)

img.save(r"test_modified.bmp")  # Save the edited image

