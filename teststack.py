import cv2
import numpy as np

im = cv2.imread("rgb_small.png")
gray = cv2.cvtColor(np.float32(im), cv2.COLOR_BGR2GRAY)
# lower = np.array([77, 77, 77], dtype="uint8")
# upper = np.array([150, 100, 30],

print(im.shape)
print(gray.shape)
upper = np.array([0, 255, 0],
                 dtype="uint8")                 # เอามาจากช่องสีที่คิดว่าเป็นดำ ถ้าเลขตำกว่านี้คือสีดำ -> อ้างอิงจาก imageprocessing.py  ยิ่งน้อยยิ่งดำ

black = 0                                       # ดูว่ามีกี่ pixel ที่คิดว่าดำ

w, h = gray.shape
# if gray.shape == (gray.shape):  # if img is grayscale, expand
#     print "convert 1-channel image to ", nchannels, " image."
#     new_img = np.zeros((height, width, nchannels))
#     for ch in range(nchannels):
#         for xx in range(height):
#             for yy in range(width):
#                 new_img[xx, yy, ch] = img[xx, yy]
#     img = new_img

# สำหรับหาพื้นที่รูป
for h in range(len(gray)):                        # loop หาพื้นที่รูป
    for w in range(len(gray[h])):
        for v in range(len(gray[h][w])):          # RGB
            if (gray[h][w][v] < upper[v]):        # เช็ตว่าถ้าเลขน้อยกว่า upper -> เป็นสีดำ
                black += 1                       # เก็บค่าสีดำ
percent = black / (w * h * 3) * 100             # (w*h)*3  -> *3 มาจาก RGB

print(str("{0}%".format(f"{percent:.2f}")))
cv2.imshow('Show',gray)
cv2.waitKey(0)
#ข้อเสีย -> รูปแสงเงา คลาดเคลื่อน
