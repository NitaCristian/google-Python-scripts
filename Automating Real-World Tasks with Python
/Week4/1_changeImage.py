#!/usr/bin/env python3
from PIL import Image
import os

src_dir = "/home/student-03-ac477d965949/supplier-data/images"

for file_name in os.listdir(src_dir):
    if ".tiff" in file_name:
        file_path = os.path.join(src_dir, file_name)
        base_name = file_name.split('.')[0]
        Image.open(file_path).resize((600, 400)).convert("RGB").save(
            "{}/{}.jpeg".format(src_dir, base_name), "JPEG")
