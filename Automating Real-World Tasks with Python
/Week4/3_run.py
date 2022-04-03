#!/usr/bin/env python3
import requests
import os

src_dir = "/home/student-03-ac477d965949/supplier-data/descriptions"
url = "http://34.133.157.81/fruits/"


def get_number(string):
    for index, char in enumerate(string):
        if char.isdigit() == False:
            return int(string[:index])


for file_name in os.listdir(src_dir):
    file_path = os.path.join(src_dir, file_name)
    base_name = file_name.split('.')[0]

    with open(file_path, 'r') as file:
        lines = file.readlines()

        supply = {"name": lines[0].strip(),
                  "weight": get_number(lines[1].strip()),
                  "description": lines[2].strip(),
                  "image_name": "{}.jpeg".format(base_name)}

        response = requests.post(url, json=supply)
