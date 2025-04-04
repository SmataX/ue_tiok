import cv2
import numpy as np
import imutils

def zad1():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("img", image)
    M = np.float32([[1, 0, 30], [0, 1, -50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Zad 1", shifted)

def zad2():
    image = cv2.imread("sad_cat.png")
    M = np.float32([[1, 0, -20], [0, 1, -50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Zad 2", shifted)

def zad3():
    image = cv2.imread("sad_cat.png")
    M = np.float32([[1, 0, image.shape[1] // 2], [0, 1, image.shape[0] // 2]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Zad 3", shifted)

def zad4():
    image = cv2.imread("sad_cat.png")
    shifted = imutils.translate(image, 100, 50)
    cv2.imshow("Zad 4", shifted)

def zad5():
    x = int(input("Przesuniecie x: "))
    y = int(input("Przesuniecie y: "))
    image = cv2.imread("sad_cat.png")
    shifted = imutils.translate(image, x, y)
    cv2.imshow("Zad 5", shifted)

if __name__ == "__main__":
    zad5()
    cv2.waitKey(0)