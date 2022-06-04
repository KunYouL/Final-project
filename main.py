import tkinter as tk
import PIL.Image
import numpy as np
from PIL import ImageTk, Image
import cv2 as cv
from tkinter import filedialog
from matplotlib import pyplot as plt
import Face1

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title('My window')
        self.window.geometry('1000x600')

        self.my_function = Face1.Myfunction()

        # Add a menubar
        self.main_menu = tk.Menu(window)  # 創建視窗

        # Add file submenu
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="開啟檔案", command=self.my_function.open_file)
        self.file_menu.add_command(label="儲存檔案", command=self.my_function.save_file)
        self.file_menu.add_separator()  # 分隔線
        self.file_menu.add_command(label="離開程式", command=window.quit)

        # Add operation1 submenu
        self.operation1_menu = tk.Menu(self.main_menu, tearoff=0)
        self.operation1_menu.add_command(label='人臉辨識', command=self.my_function.face_recognition)

        # Add operation2 submenu
        self.operation2_menu = tk.Menu(self.main_menu, tearoff=0)
        self.operation2_menu.add_command(label='小畫家', command=self.my_function.Painter)

        # Add  submenu to mainmenu
        self.main_menu.add_cascade(label="檔案", menu=self.file_menu)
        self.main_menu.add_cascade(label='功能1', menu=self.operation1_menu)
        self.main_menu.add_cascade(label='功能2', menu=self.operation2_menu)

        # display menu
        self.window.config(menu=self.main_menu)
        self.window.mainloop()

App(tk.Tk(), "OpenCv with Tkinter GUI")