import cv2
import imutils

def zad1():
    image = cv2.imread("sad_cat.png")
    r = (image.shape[1] // 2) / image.shape[1]
    dim = (image.shape[1] // 2, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized", resized)

def zad2():
    image = cv2.imread("sad_cat.png")
    r = (image.shape[1] * 2) / image.shape[1]
    dim = (image.shape[1] * 2, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resized", resized)

def zad3():
    image = cv2.imread("sad_cat.png")
    resized = cv2.resize(image, (300, 200), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resized", resized)

def zad4():
    image = cv2.imread("sad_cat.png")
    r = (image.shape[1] * 3) / image.shape[1]
    dim = (image.shape[1] * 3, int(image.shape[0] * r))
    resized1 = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
    resized2 = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    resized3 = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    resized4 = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("Resized INTER_NEAREST", resized1)
    cv2.imshow("Resized INTER_LINEAR", resized2)
    cv2.imshow("Resized INTER_CUBIC", resized3)
    cv2.imshow("Resized INTER_CUBIC", resized4)

def zad5():
    image = cv2.imread("sad_cat.png")
    resized = imutils.resize(image, width=500)
    cv2.imshow("Resized", resized)

def zad6():
    image = cv2.imread("sad_cat.png")
    resized = imutils.resize(image, height=400)
    cv2.imshow("Resized", resized)

def zad7():
    image = cv2.imread("sad_cat.png")
    resized = imutils.resize(image, width=image.shape[1] // 5, inter=cv2.INTER_AREA)
    cv2.imshow("Resized", resized)

def zad8():
    image = cv2.imread("sad_cat.png")
    resized1 = imutils.resize(image, width=image.shape[1] * 4, inter=cv2.INTER_CUBIC)
    resized2 = imutils.resize(image, width=image.shape[1] * 4, inter=cv2.INTER_LANCZOS4)
    cv2.imshow("Resized INTER_CUBIC", resized1)
    cv2.imshow("Resized INTER_LANCZOS4", resized2)

def zad9():
    image = cv2.imread("sad_cat.png")
    for i in range(100, 300, 20):
        resized = imutils.resize(image, width=round(image.shape[1] * (i / 100)), inter=cv2.INTER_CUBIC)
        cv2.imshow("Resized", resized)
        cv2.waitKey(300)

def zad10():
    image = cv2.imread("sad_cat.png")
    resized = imutils.resize(image, width=800, inter=cv2.INTER_AREA)
    cv2.imwrite("img.png", resized)


if __name__ == "__main__":
    zad10()
    cv2.waitKey(0)