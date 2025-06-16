import cv2

def zad1():
    image = cv2.imread("sad_cat.png")
    roi = image[0:100, 0:100]
    cv2.imshow("ROI 100x100 (Top-Left)", roi)

def zad2():
    image = cv2.imread("sad_cat.png")
    (h, _) = image.shape[:2]
    bottom_half = image[h//2:h, :]
    cv2.imshow("Bottom Half", bottom_half)
 
def zad3():
    image = cv2.imread("sad_cat.png")
    (_, w) = image.shape[:2]
    right_half = image[:, w//2:w]
    cv2.imshow("Right Half", right_half)

def zad4():
    image = cv2.imread("sad_cat.png")
    startX = int(input("Enter startX: "))
    endX = int(input("Enter endX: "))
    startY = int(input("Enter startY: "))
    endY = int(input("Enter endY: "))
    roi = image[startY:endY, startX:endX]
    cv2.imshow("Dynamic ROI", roi)

def zad5():
    image = cv2.imread("face.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        cv2.imshow("Face", face)
        break

def zad6():
    image = cv2.imread("sad_cat.png")
    patch = image[0:100, 0:100]
    image[100:200, 100:200] = patch
    cv2.imshow("Patched Image", image)

def zad7():
    image = cv2.imread("sad_cat.png")
    (h, w) = image.shape[:2]
    h_step = h // 3
    w_step = w // 3

    for i in range(3):
        for j in range(3):
            roi = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]
            cv2.imshow(f"Cell ({i},{j})", roi)
            cv2.waitKey(100)

def zad8():
    image = cv2.imread("sad_cat.png")
    (h, w) = image.shape[:2]
    roi_h, roi_w = 100, 100
    for x in range(0, w - roi_w, 10):
        roi = image[0:roi_h, x:x + roi_w]
        cv2.imshow("Sliding ROI", roi)
        key = cv2.waitKey(0)
        if key == 27:  # ESC
            break

def zad9():
    image = cv2.imread("sad_cat.png")
    cropped = image[0:300, 0:300]
    cv2.imshow("Cropped 300x300", cropped)
    cv2.imwrite("cropped_image.jpg", cropped)

if __name__ == "__main__":
    zad6()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
