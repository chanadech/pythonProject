import cv2
import os
import numpy as np
from os import listdir

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


#main
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

