import PIL.Image
from PIL import Image
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

    def face_recognition(self):  # 臉部偵測
        src = self.open_file1()
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        imgrect = faceCascade.detectMultiScale(gray, 1.1, 5)  # 辨識眼  elon(2.2, 8) ppl(1.1, 5) aks(1.1, 3)
        # 參數(掃得圖，每檢測完擴大繼續掃，成功檢測次數(越多次可能仔細，導致可能找不到))
        print(len(imgrect))  # 看偵測幾張

        for (x, y, w, h) in imgrect:  # 可能多部位 用迴圈跑
            cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow('face', src)  # 顯示圖片

    def concatenate(self):  # 圖片合併
        src1 = self.open_file1()
        src2 = self.open_file1()

        src1 = cv.resize(src1, (250, 200))  # 將圖片大小設置為 250 * 200
        src2 = cv.resize(src2, (250, 200))

        image = np.concatenate((src1, src2))
        cv.imshow('image', image)

    def blending(self):  # 圖片重疊
        src1 = self.open_file1()
        src2 = self.open_file1()

        src1 = cv.resize(src1, (250, 200))
        src2 = cv.resize(src2, (250, 200))

        blend = cv.addWeighted(src1, 0.6, src2, 0.4, 0)  #
        cv.imshow('blend', blend)


    def drawing(self):
        src = self.open_file1()
        dots = []  # 記錄座標的空串列
        def show_xy(event, x, y, flags, param):
            if event == 1:
                dots.append([x, y])  # 紀錄座標
                cv.circle(src, (x, y), 10, (0, 0, 255), -1)  # 在點擊的位置，繪製圖形
                num = len(dots)   # 目前有幾個座標
                if num > 1:  # 如果有兩點以上
                    x1 = dots[num - 2][0]
                    y1 = dots[num - 2][1]
                    x2 = dots[num - 1][0]
                    y2 = dots[num - 1][1]
                    cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)  #取得最後的兩個座標，繪製直線
                cv.imshow('src', src)

        cv.imshow('src', src)
        cv.setMouseCallback('src', show_xy)
        cv.waitKey(0)

