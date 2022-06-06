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

    def concatenate(self):
        src1 = self.open_file1()
        src2 = self.open_file1()

        image = np.concatenate((src1, src2))
        cv.imshow('image', image)

