import os
import random
import shutil

from torchvision import datasets, transforms

from modules.image_converter import convert_directory_image_formats, resize_images, rotate_images
from modules.baseline_resnet50 import BaselineResNet50


def prepare_database(size: int, rotation_step: int, val_percentage: float):
    raw_unconverted = "data/raws/unconverted"
    raw_converted = "data/raws/converted"
    resized_dir = f"data/x{size}"
    complete_dir = f"data/complete/x{size}"
    train_dir = os.path.join(complete_dir, "train")
    val_dir = os.path.join(complete_dir, "val")

    # Step 1: Convert and resize
    convert_directory_image_formats(raw_unconverted, raw_converted, "jpg")
    resize_images(raw_converted, resized_dir, size)

    # Step 2: Apply rotations
    for angle in range(0, 360, rotation_step):
        rotate_images(resized_dir, complete_dir, angle)

    # Step 3: Organize into class folders (initially in train/)
    image_files = [
        f for f in os.listdir(complete_dir)
        if os.path.isfile(os.path.join(complete_dir, f)) and '_' in f
    ]

    for file in image_files:
        parts = file.split('_')
        if len(parts) < 2:
            continue  # skip files with unexpected names
        class_name = parts[0]
        src = os.path.join(complete_dir, file)
        class_train_dir = os.path.join(train_dir, class_name)
        os.makedirs(class_train_dir, exist_ok=True)
        shutil.move(src, os.path.join(class_train_dir, file))

    # Step 4: Split training data into validation set per class
    for class_name in os.listdir(train_dir):
        class_train_path = os.path.join(train_dir, class_name)
        if not os.path.isdir(class_train_path):
            continue

        images: list[str] = os.listdir(class_train_path)
        random.shuffle(images)

        val_count = round(len(images) * val_percentage)
        val_images = images[:val_count]

        class_val_path = os.path.join(val_dir, class_name)
        os.makedirs(class_val_path, exist_ok=True)

        for file in val_images:
            shutil.move(
                os.path.join(class_train_path, file),
                os.path.join(class_val_path, file)
            )
        print(f"Moved {len(images) - val_count} to train/{class_name}, {val_count} to val/{class_name}")


if __name__ == '__main__':
    size = 224

    # prepare_database(size=size, rotation_step=15, val_percentage=0.15)
    resnet = BaselineResNet50(size=size, data_path=f'data/complete/x{size}', batch_size=32)
    resnet.train(num_epochs=5)
    resnet.evaluate()