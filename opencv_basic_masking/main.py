import cv2
import numpy as np

def zad1():
    image = cv2.imread("face.png")
    mask = np.zeros(image.shape[:2], dtype="uint8")
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    cv2.ellipse(mask, center, (w//4, h//3), 0, 0, 360, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Original", image)
    cv2.imshow("Masked (only face)", masked)


def zad2():
    image = cv2.imread("face.png")
    masked = image.copy()
    (h, w) = image.shape[:2]
    eye_mask = cv2.rectangle(masked, (w//4, h//3), (3*w//4, h//2), (0, 0, 0), -1)
    cv2.imshow("Original", image)
    cv2.imshow("Eyes Hidden", masked)


def zad3():
    image = cv2.imread("flowers.png")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([160, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original", image)
    cv2.imshow("Red Color Extracted", result)


if __name__ == "__main__":
    zad3()
    cv2.waitKey()
    cv2.destroyAllWindows()