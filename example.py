from PIL import Image
from quality import get_quality

image = Image.open(open('examples/1.jpg'))
print get_quality(image)

image = Image.open(open('examples/75.jpg'))
print get_quality(image)

image = Image.open(open('examples/90.jpg'))
print get_quality(image)

image = Image.open(open('examples/100.jpg'))
print get_quality(image)

