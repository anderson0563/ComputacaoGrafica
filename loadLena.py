from PIL import Image
im = Image.open("./lena.jpeg")
display(im)
im = im.rotate(45)
display(im)