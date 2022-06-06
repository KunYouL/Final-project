import cv2 as cv
import numpy as np

drawing = False  # 如果點擊滑鼠，為真
mode = True  # 如果為真，繪製矩形，按m可以切成
ix, iy = -1, -1
ox, oy = -1, -1


def draw_circle(event, x, y, flags, param):  # mouse callback function
    global ix, iy, ox, oy, drawing, mode

    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):  # 按下m可以切換畫圖的圖形
        mode = not mode
    elif k == 27: # 按下Ese離開程式
        break

cv.destroyAllWindows()