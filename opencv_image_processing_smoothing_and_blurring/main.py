import cv2
import numpy as np

def zad1():
    image = cv2.imread("sad_cat.jpg")
    cv2.imshow("Original", image)
    value = 5

    img_blur = cv2.blur(image, (3, 3))
    img_gaussian_blur = cv2.GaussianBlur(image, (value, value), 1)
    img_median_blur = cv2.medianBlur(image, value)
    img_bilateral_filter = cv2.bilateralFilter(image, 11, 21, 7)
    cv2.imshow("img_blur", img_blur)
    cv2.imshow("img_gaussian_blur", img_gaussian_blur)
    cv2.imshow("img_median_blur", img_median_blur)
    cv2.imshow("img_bilateral_filter", img_bilateral_filter)
    
    # 1. medianBlur
    # 2. bilateralFilter

def zad2():
    image = cv2.imread("sad_cat.jpg")
    cv2.imshow("Original", image)
    kernelSizes = [(3, 3), (9, 9), (15, 15)]
    
    for (kX, kY) in kernelSizes:
        blurred = cv2.blur(image, (kX, kY))
        cv2.imshow("Average ({}, {})".format(kX, kY), blurred)

def zad3():
    image = cv2.imread("sad_cat.jpg")
    params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
    for (diameter, sigmaColor, sigmaSpace) in params:
        img_bilateral_filter = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        cv2.imshow(f"img_bilateral_filter ({diameter} {sigmaColor} {sigmaSpace})", img_bilateral_filter)

def zad4():
    image = cv2.imread("image.jpg")

    blur = cv2.blur(image, (5, 5))
    gblur = cv2.GaussianBlur(image, (5, 5), 0)
    mblur = cv2.medianBlur(image, 5)
    bblur = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Original", image)
    cv2.imshow("Blur", blur)
    cv2.imshow("Gaussian", gblur)
    cv2.imshow("Median", mblur)
    cv2.imshow("Bilateral", bblur)
    
    # 1. img_median_blur
    # 2. img_bilateral_filter

def zad5():
    image = cv2.imread("image.jpg")

    blur = cv2.blur(image, (5, 5))
    gblur = cv2.GaussianBlur(image, (5, 5), 0)
    mblur = cv2.medianBlur(image, 5)
    bblur = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Original", image)
    cv2.imshow("Blur", blur)
    cv2.imshow("Gaussian", gblur)
    cv2.imshow("Median", mblur)
    cv2.imshow("Bilateral", bblur)

def zad6():
    image = cv2.imread("portrait.png")

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (100, 100), (400, 400), 255, -1)  # maska na osobę

    blurred = cv2.GaussianBlur(image, (21, 21), 0)
    result = np.where(mask[:, :, np.newaxis] == 255, image, blurred)

    cv2.imshow("Original", image)
    cv2.imshow("Simulated DoF", result)


if __name__ == "__main__":
    zad6()
    cv2.waitKey(0)