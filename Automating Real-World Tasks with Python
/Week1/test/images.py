# Import module to work with images
from PIL import Image

# Load the image into a variable
im = Image.open('image.jpg')

# Rotate image 45 degree counterclockwise
im.rotate(45)

# Open the image and display it
im.show()

# Resize the image
new_im = im.resize((640, 480))

# Save the new image
new_im.save('new_image.jpg')
