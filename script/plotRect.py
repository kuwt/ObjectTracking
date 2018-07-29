import os
import cv2

###############################
#  Input
###############################
#imagesTxTPath = r"E:\SourceCode\ObjectTracking\asms\build\Release\images.txt"
#RectTxTPath = r"E:\SourceCode\ObjectTracking\asms\build\Release\output.txt"

imagesTxTPath = r"E:\SourceCode\ObjectTracking\kcf\build\Release\images.txt"
RectTxTPath = r"E:\SourceCode\ObjectTracking\kcf\build\Release\\output.txt"
###############################
#  Util
###############################
def readtxtFile(fname):
    with open(fname) as f:
        content = f.read().splitlines()
        #content = f.readlines()
    return content
###############################
#  main
###############################
def plotRect():
    imgContent = readtxtFile(imagesTxTPath)
    rectContent = readtxtFile(RectTxTPath)
    for idx,imgStr in enumerate(imgContent):
        rectList = rectContent[idx].split(",")
        img = cv2.imread(imgStr)
        cv2.rectangle(img, ( int(rectList[0]),  int(rectList[1])), (int(rectList[0]) + int(rectList[2]), int(rectList[1]) + int(rectList[3])), (255, 0, 0), 2)
        cv2.imshow("img",img)
        cv2.waitKey()

if __name__ == "__main__":
    plotRect()
