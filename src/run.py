from modules.image_converter import convert_directory_image_formats, resize_images, rotate_images


def prepare_database():
    convert_directory_image_formats("data/raws/unconverted", "data/raws/converted", "jpg")
    for size in [32, 64]:
        resize_images("data/raws/converted", f"data/x{size}", size)
        for rotation in range(0, 360, 90):
            rotate_images(f"data/x{size}", f"data/complete/x{size}", rotation)


if __name__ == '__main__':
    prepare_database()