#!/usr/bin/env python3
from PIL import Image
import os

src_dir_path = "{}/images/".format(os.environ['HOME'])
dest_dir_path = "/opt/icons/"

if not os.path.exists(dest_dir_path):
    os.makedirs(dest_dir_path)

for file in os.listdir(src_dir_path):
    file_path = os.path.join(src_dir_path, file)
    # os.rename(file_path, file_path + ".jpeg")

    Image.open(file_path).resize(
        (128, 128)).rotate(-90).convert('RGB').save("{}{}".format(dest_dir_path, file), "JPEG")
