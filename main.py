import cv2

def main():
    image = cv2.imread("cat.png")

    if image is None:
        print("File not found!")
        return
    
    image_gray = cv2.imread("cat.png", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("cat_sad.png", image_gray)

    color_img_channels = image.shape[-1]
    gray_img_channels = 1

    print(f'Color image channels: {color_img_channels}')
    print(f'Color image channels: {gray_img_channels}')

    cv2.namedWindow("Display", cv2.WINDOW_NORMAL) 
    cv2.imshow("color image ", image)
    cv2.imshow("gray image", image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()