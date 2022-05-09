from PIL import Image, ImageOps
import os
import glob

IMAGES_PATH = glob.glob('*.jpg') #globaliame faile turn_images_grey

for image in IMAGES_PATH:
	with open(image, 'rb') as file:
		img = Image.open(file)
		file_name, file_extension = os.path.splitext(image)
		grey_image = ImageOps.grayscale(img)
		grey_image.save('images/{}.jpg'.format(file_name))
