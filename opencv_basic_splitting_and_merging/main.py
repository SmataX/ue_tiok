import cv2

def zad1():
    image = cv2.imread("flowers.jpg")
    (B, G, R) = cv2.split(image)
    cv2.imwrite("B.jpg", B)
    cv2.imwrite("G.jpg", G)
    cv2.imwrite("R.jpg", R)

def zad3():
    image = cv2.imread("flowers.jpg")
    (B, G, R) = cv2.split(image)
    merged = cv2.merge([R, B, G])
    cv2.imshow("Merged", merged)
    merged2 = cv2.merge([R, cv2.add(B, -10000), G])
    cv2.imshow("Merged2", merged2)

def zad4():
    image = cv2.imread("flowers.jpg")
    (B, G, R) = cv2.split(image)
    merged = cv2.merge([cv2.add(R, 100), B, G])
    cv2.imshow("Merged", merged)

def zad5():
    pass

def zad6():
    image = cv2.imread("logo.png")
    (B, G, R) = cv2.split(image)
    merged = cv2.merge([R, B, G])
    cv2.imshow("Merged", merged)


zad6()
cv2.waitKey(0)