import cv2
import numpy as np

im = cv2.imread("jp black inversed.png")
upper = np.array([255, 255, 255], dtype="uint8")

black = 0
w, h, x = im.shape                              # สำหรับหาพื้นที่รูป
for h in range(len(im)):                        # loop หาพื้นที่รูป
    for w in range(len(im[h])):
        for v in range(len(im[h][w])):          # RGB
            if im[h][w][v] < upper[v]:        # เช็ตว่าถ้าเลขน้อยกว่า upper -> เป็นสีดำ
                black += 1                       # เก็บค่าสีดำ
percent = black / (w * h * 3) * 100             # (w*h)*3  -> *3 มาจาก RGB

print(str("{0}%".format(f"{percent:.2f}")))

#ข้อเสีย -> รูปแสงเงา คลาดเคลื่อน


