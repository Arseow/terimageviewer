from PIL import Image
import random
import os
import time
import sys

img = Image.open(sys.argv[1])
print(img.height, img.width, img.height * img.width, img.mode)
img.convert('RGB')
pixels = []
positions = []

# TODO - improve anim, fix bug with height and width

# anim fucntion is not fully completed, it can have some bugs or usless lines in it

def show_anim(img):
    images = anim(img, 32) # change the size of your image scale
    
    for image in images:
        show_image(image)
        time.sleep(1)
        os.system('clear')

def anim(img, scale):
    images = []
    
    corpint = 0
    
    while corpint <= img.width:
        images.append(img.crop((corpint, 0, corpint + scale, 32)))
        corpint += 32
    
    return images
       
def show_image(img):
    for y in range(img.height):
        for x in range(img.width):
            positions.append([x, y])
            color = img.getpixel((x, y))
            pixels.append(color)

    def randomize():
        return random.randint(1000, 9000)
    
    hash_color = {} # example pixel: unicode
    for i in list(set(pixels)):
        hash_color[str(i)] = chr(randomize())

    curr_y = 0

    for i, n in enumerate(pixels):
        if positions[i][1] > curr_y:
            print()
            curr_y += 1
        
        print(hash_color[str(n)], end="")

if sys.argv[2] == 'anim':
    show_anim(img)
else:
    show_image(img)