import cv2
import os
import numpy as np
from os import listdir


# get the path or directory
# folder_dir = "/home/chanadech/PycharmProjects/pythonProject/dataset1"
# for images in os.listdir(folder_dir):
#
#     # check if the image ends with png or jpg or jpeg
#     if (images.endswith(".png") or images.endswith(".jpg") \
#             or images.endswith(".jpeg")):
#         # display
#         print(images)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


imgs = []


def calculateData(file):
    im = cv2.imread(file)
    upper = np.array([255, 255, 255], dtype="uint8")
    black = 0
    w, h, x = im.shape
    for h in range(len(im)):
        for w in range(len(im[h])):
            for v in range(len(im[h][w])):
                if im[h][w][v] < upper[v]:
                    black += 1
    percent = black / (w * h * 3) * 100
    print(str("{0}%".format(f"{percent:.2f}")))


# main
while True:
    file = input("Input filename >>> ")
    if file == "exit":
        print(imgs)
        break

    if os.path.exists(file):
        img = cv2.imread(file)
        imgs.append(img)
        calculateData(file)

    else:
        print("File not found.")

# calculateData(load_images_from_folder("/home/chanadech/PycharmProjects/pythonProject/dataset1"))
