import PIL.Image
from PIL import Image, ImageTk
import tkinter as tk
import cv2 as cv
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import math

class Myfunction:
    def open_file1(self):
        filetypes = (
            ('png file', '*.png'),
            ('jpg file', '*.jpg'),
            ('All file', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        img = cv.imread(filename)
        return img

    def open_file(self):
        filetypes = (
            ('png file', '*.png'),
            ('jpg file', '*.jpg'),
            ('All file', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Open a file1',
            initialdir='/',
            filetypes=filetypes
        )
        img = cv.imread(filename)
        cv.imshow('img', img)
        cv.waitKey()

    def save_file(self):
        pass

    def face_recognition(self):
        src = self.open_file1()
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        imgrect = faceCascade.detectMultiScale(gray, 1.1, 5)  # 辨識眼  elon(2.2, 8) ppl(1.1, 5) aks(1.1, 3)
        # 參數(掃得圖，每檢測完擴大繼續掃，成功檢測次數(越多次可能仔細，導致可能找不到))
        print(len(imgrect))  # 看偵測幾張

        for (x, y, w, h) in imgrect:  # 可能多部位 用迴圈跑
            cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow('face', src)  # 顯示圖片



    def Painter(self):
        drawing = False
        mode = True
        start = (-1, -1)
        def mouse_event(event, x, y, flages, param):
            global  start, drawing, mode

            if event == cv.EVENT_LBUTTINDIWN:
                drawing = True
                start = (x, y)
            elif event == cv.EVENT_MOUSEMOVE:
                if drawing:
                    if mode:
                        cv.rectangle(img,start, (x, y), (0, 255, 0), -1)
                    else:
                        cv.circle(img, (5, 255), -1)
                elif event == cv.EVENT_LBUTTONUP:
                    drawing = False
                    if mode:
                        cv.rectangle(img, -1)
                    else:
                        cv.circle(img, -1)

        img = np.zeros((512, 512, 3), np.unit8)
        cv.namedWindow('image')
        cv.setMouseCallback('image', mouse_event)

        while(True):
            cv.imshow('image', img)

            if cv.waitkey(1) == ord('m'):
                mode = not mode
            elif cv.waitkey(1) == 27:
                break
