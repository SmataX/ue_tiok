import cv2
import numpy

class colors:
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    WHITE = (255, 255, 255)

def zad1():
    canvas = numpy.zeros((500, 300, 3), dtype="uint8")
    cv2.line(canvas, (0, 0), (len(canvas[0]), len(canvas)), colors.BLUE, 2)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

def zad2():
    canvas = numpy.zeros((400, 400, 3), dtype="uint8")
    cv2.rectangle(canvas, (0, 0), (100, 50), colors.GREEN)
    cv2.rectangle(canvas, (300, 350), (400, 400), colors.RED, 3)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

def zad3():
    canvas = numpy.zeros((300, 300, 3), dtype="uint8")
    cv2.circle(canvas, (0, 0), 40, colors.BLUE)
    cv2.circle(canvas, (150, 150), 40, colors.RED)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

def zad4():
    canvas = numpy.zeros((300, 300, 3), dtype="uint8")
    cv2.rectangle(canvas, (100, 100), (200, 200), colors.GREEN)
    cv2.circle(canvas, (150, 150), 30, colors.RED)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

def zad5():
    canvas = numpy.zeros((300, 300, 3), dtype="uint8")
    size = 20

    while size <= 300:
        cv2.rectangle(canvas, (150 - size // 2, 150 - size // 2), (150 + size // 2, 150 + size // 2), colors.RED, 2)

        size += 20
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

def zad6():
    canvas = numpy.zeros((300, 500, 3), dtype="uint8")
    cv2.rectangle(canvas, (0, 0), (500, 300), colors.RED, -1)
    cv2.circle(canvas, (250, 150), 120, colors.WHITE, -1)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)


if __name__ == "__main__":
    zad6()