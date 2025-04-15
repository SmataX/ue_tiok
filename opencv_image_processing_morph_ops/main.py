import cv2

def zad1():
    image = cv2.imread('logo.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range(0, 3):
        eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
        cv2.imshow("Eroded {} times".format(i + 1), eroded)


def zad2():
    image = cv2.imread('logo.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
        cv2.imshow("Dilated {} times".format(i + 1), dilated)

def zad3():
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    image = cv2.imread('logo.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)

def zad4():
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    image = cv2.imread('logo.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)

def zad5():
    image = cv2.imread('logo.png')
    image2 = None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image2 = cv2.erode(gray.copy(), None, iterations=10)
    image2 = cv2.dilate(image2.copy(), None, iterations=10)
    image2 = cv2.morphologyEx(image2.copy(), cv2.MORPH_OPEN, (7, 7))
    image2 = cv2.morphologyEx(image2.copy(), cv2.MORPH_CLOSE, (7, 7))
    cv2.imshow("sadas", image2)

def zad6():
    image = cv2.imread('tablica.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Tablica - gray", gray)
    img = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, (7, 7))
    cv2.imshow("Tablica - open", img)


zad6()
cv2.waitKey(0)