import cv2 as cv

img = cv.imread('photo/123.jpg')   #讀圖片
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   #轉灰階
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')   #載入辨識模型
imgrect = faceCascade.detectMultiScale(gray, 1.1, 5)   #辨識眼  elon(2.2, 8) ppl(1.1, 5) aks(1.1, 3)
#參數(掃得圖，每檢測完擴大繼續掃，成功檢測次數(越多次可能仔細，導致可能找不到))
print(len(imgrect)) #看偵測幾張

for(x, y, w, h) in imgrect:        #可能多部位 用迴圈跑
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('img', img)     #顯示圖片

cv.waitKey()