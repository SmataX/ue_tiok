import argparse
import imutils
import cv2

def zad1():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)


def zad2():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by -90 Degrees", rotated)

def zad3():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    (h, w) = image.shape[:2]
    M = cv2.getRotationMatrix2D((0, 0), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)

def zad4():
    angle = int(input("Rotate by: "))

    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"Rotated by {angle} Degrees", rotated)

def zad5():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    rotated = imutils.rotate(image, 180)
    cv2.imshow("Rotated by 180 Degreed", rotated)


def zad6():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)
    rotated = imutils.rotate_bound(image, -33)
    cv2.imshow("Rotated by -33 Degreed", rotated)

def zad7():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
    rotated1 = cv2.warpAffine(image, M, (w, h))

    rotated2 = imutils.rotate_bound(image, 60)
    cv2.imshow("Rotated by 60 Degreed 1", rotated1)
    cv2.imshow("Rotated by 60 Degreed 2", rotated2)

def zad8():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    
    for _ in range(3):
        M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
        rotated1 = cv2.warpAffine(image, M, (w, h))
    M = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
    rotated2 = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Rotated by 90 Degreed 1", rotated1)
    cv2.imshow("Rotated by 90 Degreed 2", rotated2)

def zad9():
    image = cv2.imread("sad_cat.png")
    rotated = imutils.rotate_bound(image, 75)
    cv2.imshow("Rotated by 75 Degreed", rotated)
    cv2.imwrite("img.png", rotated)

def zad10():
    image = cv2.imread("sad_cat.png") 
    for angle in range(0, 360, 15):
        rotated = imutils.rotate_bound(image, angle)
        cv2.imshow("Rotated", rotated)
        cv2.waitKey(50)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    zad10()
    cv2.waitKey(0)
    cv2.destroyAllWindows()