import cv2
import numpy as np

def zad1():
    input = np.zeros((500, 500), dtype="uint8")

    pts = np.array([[100, 400], [400, 400], [250, 100]], np.int32)
    triangle = cv2.fillPoly(input.copy(), [pts], 255)
    circle = cv2.circle(input.copy(), (250, 250), 150, 255, -1)

    ex1_and = cv2.bitwise_and(triangle, circle)
    ex1_or = cv2.bitwise_or(triangle, circle)
    ex1_xor = cv2.bitwise_xor(triangle, circle)
    ex1_not_triangle = cv2.bitwise_not(triangle)
    ex1_not_circle = cv2.bitwise_not(circle)

    cv2.imshow('Triangle', triangle)
    cv2.imshow('Circle', circle)
    cv2.imshow('AND', ex1_and)
    cv2.imshow('OR', ex1_or)
    cv2.imshow('XOR', ex1_xor)
    cv2.imshow('NOT Triangle', ex1_not_triangle)
    cv2.imshow('NOT Circle', ex1_not_circle)

    cv2.imwrite('TriaCircle.jpg', ex1_and)
    cv2.imwrite('circle.jpg', circle)


def zad2():
    img1 = cv2.imread('TriaCircle.jpg')
    img2 = cv2.imread('circle.jpg')

    xor_diff = cv2.bitwise_xor(img2, img1)

    cv2.imshow('TriaCircle', img1)
    cv2.imshow('Circle', img2)
    cv2.imshow('XOR Difference', xor_diff)

if __name__ == "__main__":
    zad2()
    cv2.waitKey()
    cv2.destroyAllWindows()