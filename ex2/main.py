import cv2



def zad1():
    image = cv2.imread("sad_cat.png") 
    pixel = image[0, 0]
    print(f"Pixel [0, 0]: R={pixel[2]}, G={pixel[1]}, B={pixel[0]}")

def zad2():
    image = cv2.imread("sad_cat.png") 
    cv2.imshow("img", image)
    image[-1, -1] = (0, 0, 255)
    cv2.imshow("img_changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad3():
    image = cv2.imread("sad_cat.png") 
    center = (round(image.shape[1] / 2), round(image.shape[0] / 2))
    pixel = image[center[0], center[1]]
    print(f"Pixel [{center[0]}, {center[1]}]: R={pixel[2]}, G={pixel[1]}, B={pixel[0]}")

def zad4():
    image = cv2.imread("sad_cat.png") 
    pos_x = int(input(f"Enter x position <0, {image.shape[1]}>: "))
    while pos_x not in range(0, image.shape[1]):
        pos_x = int(input(f"Enter x position <0, {image.shape[1]}>: "))

    pos_y = int(input(f"Enter y position <0, {image.shape[0]}>: "))
    while pos_y not in range(0, image.shape[1]):
        pos_y = int(input(f"Enter y position <0, {image.shape[0]}>: "))

    image[pos_x, pos_y] = (0, 0, 0)

def zad5():
    image = cv2.imread("sad_cat.png") 
    center = (round(image.shape[1] / 2), round(image.shape[0] / 2))
    for i in range(0, center[0]):
        for j in range(0, center[1]):
            image[j, i] = (255, 0, 0)
    
    cv2.imshow("img_changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad6():
    image = cv2.imread("sad_cat.png") 
    center = (round(image.shape[1] / 2), round(image.shape[0] / 2))
    for i in range(center[0] - 50, center[0] + 50):
        for j in range(center[1] - 50, center[1] + 50):
            image[j, i] = (255, 0, 0)
    
    cv2.imshow("img_changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad7():
    image = cv2.imread("sad_cat.png")
    size = image.shape[1] // 9
    imgs = []
    for i in range(9):
        start = i * size
        end = start + size
        img_part = image[:, start:end]
        imgs.append(img_part)
        cv2.imshow(f"Img {i}", img_part)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad8():
    image = cv2.imread("sad_cat.png") 
    cv2.imshow(f"Img", image)
    for i in range(image.shape[1]):
        image[100, i] = (0, 255, 0)
    
    cv2.imshow(f"Img2", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad9():
    image = cv2.imread("sad_cat.png") 
    for i in range(50, 100):
        for j in range(50, 100):
            image[j, i] = (255, 255, 255)
    
    cv2.imshow("img_changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad10():
    image = cv2.imread("sad_cat.png") 
    p1 = image[50, 50]
    p2 = image[200, 200]

    print(f"Pixel 1 [50, 50]: R={p1[2]}, G={p1[1]}, B={p1[0]}")
    print(f"Pixel 2 [200, 200]: R={p2[2]}, G={p2[1]}, B={p2[0]}")
    diff = (int(p1[2]) - int(p2[2]), int(p1[1]) - int(p2[1]), int(p1[0]) - int(p2[0]))
    print(f"p1 - p2 = (R={diff[0]}, G={diff[1]}, B={diff[2]})")

def zad11():
    image = cv2.imread("sad_cat.png", cv2.IMREAD_GRAYSCALE) 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image)
    print(f"Pixel at {max_loc}, value {max_val}")




# zad1()
# zad2()
# zad3()
# zad4()
# zad5()
# zad6()
# zad7()
# zad8()
# zad9()
# zad10()
zad11()




