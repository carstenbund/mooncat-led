#
# Display mooncats on LED matrix 32x32
# needs rgbmatrix : https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python
#
#
import sys
sys.path.insert(0, "/home/carsten/.local/lib/python3.7/site-packages")
#print(sys.path)

import os, time
#import binascii
import cv2
import numpy as np
import random
import mooncatparser as mc
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 4

matrix = RGBMatrix(options = options)

# reads index of all rescued cats and returns list
def read_rescued():
    data = []
    with open('rescued.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            if line == "":
                break
            #print(line)
            id, line = line.split(";")
            line = line.replace('"',"")
            line = line.replace("\n","")
            data.append(line)
    return data

digits = '0123456789'
letters = 'abcdef'
all_chars = digits + letters
length = 8

matrix.brightness = 50

transp = True
scale = 10

rescued_ids = read_rescued()

while True:
    index = int(random.random()*25440)
    # only rescued
    catId = random.choice(rescued_ids)

    # out of 4bn
    #catId = "0x00" + ''.join(random.choice(all_chars) for i in range(length))

    print("catId: ", catId)
    img = mc.mooncat_render(catId, scale, transp)
    img = (img).astype('uint8')
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    img_32 = cv2.resize(img,(32,32), interpolation = cv2.INTER_NEAREST)
    img = Image.fromarray(img_32)
    matrix.SetImage(img)
    time.sleep(random.random()*4+1)
    #time.sleep(.3)


