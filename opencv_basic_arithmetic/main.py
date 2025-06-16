import cv2
import numpy as np

def zad1():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    brighter_numpy = np.clip(image + 50, 0, 255).astype(np.uint8)
    brighter_opencv = cv2.add(image, np.ones_like(image) * 50)

    cv2.imshow("Brighter (NumPy)", brighter_numpy)
    cv2.imshow("Brighter (OpenCV)", brighter_opencv)

def zad2():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    overexposed_numpy = np.clip(image + 150, 0, 255).astype(np.uint8)
    overexposed_opencv = cv2.add(image, np.ones_like(image) * 150)

    cv2.imshow("Overexposed (NumPy)", overexposed_numpy)
    cv2.imshow("Overexposed (OpenCV)", overexposed_opencv)

def zad3():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    dark_numpy = np.clip(image - 80, 0, 255).astype(np.uint8)
    dark_opencv = cv2.subtract(image, np.ones_like(image) * 80)

    cv2.imshow("Darkened (NumPy)", dark_numpy)
    cv2.imshow("Darkened (OpenCV)", dark_opencv)

def zad4():
    image = cv2.imread("sad_cat.png")
    cv2.imshow("Original", image)

    (B, G, R) = cv2.split(image)
    R = cv2.add(R, 30)
    G = cv2.subtract(G, 20)
    B = cv2.add(B, 10)

    filtered = cv2.merge([B, G, R])
    cv2.imshow("Instagram-style Filter", filtered)

def zad5():
    image1 = cv2.imread("scene1.png")  # Upewnij się, że pliki istnieją
    image2 = cv2.imread("scene2.png")
    
    if image1.shape != image2.shape:
        print("Images must have the same dimensions.")
        return

    diff = cv2.absdiff(image1, image2)
    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)
    cv2.imshow("Difference", diff)

if __name__ == "__main__":
    zad5()
    cv2.waitKey()
    cv2.destroyAllWindows()