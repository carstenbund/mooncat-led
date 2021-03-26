import mooncatparser as mc
import cv2

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

TRANSPARENT = True
SCALE = 40 # x

id_array = ["0x00768d3a11","0x00b0bfaf9c","0x00cf5c2fbc","0x0052e14510","0x00de9a2887"]
#id_array = ["0x00798d3a11"]
#id_array = ["0x0000000000"]
#id_array = read_rescued()


def test_parse(id_array, scale=20, transp=True):
    x =0
    y=0
    pose = 0
    for catId in id_array:
        img = mc.mooncat_render(catId, scale, transp)
        img_name = str(catId)
        print(img_name)
        cv2.imwrite("images/" + img_name + '.png',img)

test_parse(id_array, SCALE, TRANSPARENT)