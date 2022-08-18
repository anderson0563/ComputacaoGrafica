from PIL import Image
import random
img = Image.new('RGB', (100, 100))
white = (255,255,255)
black = (0, 0, 0)
color = white
for x in range(0, 100):
  for y in range(0, 100):
    color = random.randrange(0, 255, 1)
    img.putpixel((x,y), (color, color, color))
display(img)