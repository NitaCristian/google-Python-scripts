#!/usr/bin/env python3
import requests
import os

src_dir = "/home/student-03-ac477d965949/supplier-data/images"
url = "http://34.133.157.81/upload/"

for file_name in os.listdir(src_dir):
    if ".jpeg" in file_name:
        file_path = os.path.join(src_dir, file_name)

        with open(file_path, 'rb') as opened:
            response = requests.post(url, files={'file': opened})
