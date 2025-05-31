import cv2
import os

def convert_image_format(source_path: str, output_path: str, target_format: str) -> None:
    """
    Converts a single image file to the specified format.

    Args:
        source_file (str): Path to the input image file.
        output_path (str): Path to the directory where the converted file will be saved.
        target_format (str): Desired file format.

    Returns:
        None
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image = cv2.imread(source_path)
    if image is None:
         raise ValueError(f"Failed to load an image: {source_path}")
    
    file_name = os.path.basename(source_path).split('.')[0]
    cv2.imwrite(os.path.join(output_path, f"{file_name}.{target_format}"), image)

def convert_directory_image_formats(source_path: str, output_path: str, target_format: str) -> None:
    """
    Converts all image files in a directory to the specified format.

    Args:
        source_dir (str): Path to the directory containing input image files.
        output_dir (str): Path to the directory where converted files will be saved.
        target_format (str): Desired file format.

    Returns:
        None
    """
        
    for file in os.listdir(source_path):
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            try:
                convert_image_format(file_path, output_path, target_format)
            except ValueError as e:
                print(f"Skipping file {file}: {e}")

def resize_image(source_path: str, output_path: str, target_size: int) -> None:
    """
    Resize a single image to a square of the specified target size while maintaining aspect ratio,
    and save it to the output path.

    Parameters:
    - source_path (str): Path to the source image file.
    - output_path (str): Path where the resized image will be saved.
    - target_size (int): The desired width and height (in pixels) for the output image.

    Returns:
    - None
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image = cv2.imread(source_path)
    if image is None:
         raise ValueError(f"Failed to load an image: {source_path}")
    
    file_name, file_format = os.path.basename(source_path).split('.')
    r = target_size / image.shape[1]
    dim = (target_size, int(image.shape[0] * r))
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(output_path, f"{file_name}_x{target_size}.{file_format}"), resized_image)


def resize_images(source_path: str, output_path: str, target_size: int) -> None:
    """
    Resize all images in the given source directory to the specified target size and
    save them to the output directory.

    Parameters:
    - source_path (str): Path to the directory containing the original images.
    - output_path (str): Path to the directory where resized images will be saved.
    - target_size (int): The desired width and height (in pixels) for the output images.

    Returns:
    - None
    """
    for file in os.listdir(source_path):
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            try:
                resize_image(file_path, output_path, target_size)
            except ValueError as e:
                print(f"Skipping file {file}")


def rotate_image(source_path: str, output_path: str, target_rotation: int) -> None:
    """
    Rotate a single image by the specified number of degrees and save it to the output path.

    Parameters:
    - source_path (str): Path to the source image file.
    - output_path (str): Path where the rotated image will be saved.
    - target_rotation (int): Rotation angle in degrees (clockwise).

    Returns:
    - None
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image = cv2.imread(source_path)
    if image is None:
         raise ValueError(f"Failed to load an image: {source_path}")

    file_name, file_format = os.path.basename(source_path).split('.')
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), target_rotation, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    cv2.imwrite(os.path.join(output_path, f"{file_name}_r{target_rotation}.{file_format}"), rotated_image)

def rotate_images(source_path: str, output_path: str, target_rotation: int) -> None:
    """
    Rotate all images in the given source directory by the specified angle and save them
    to the output directory.

    Parameters:
    - source_path (str): Path to the directory containing the original images.
    - output_path (str): Path to the directory where rotated images will be saved.
    - target_rotation (int): Rotation angle in degrees (clockwise).

    Returns:
    - None
    """

    for file in os.listdir(source_path):
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            try:
                rotate_image(file_path, output_path, target_rotation)
            except ValueError as e:
                print(f"Skipping file {file}: {e}")
