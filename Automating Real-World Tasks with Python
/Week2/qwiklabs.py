#!/usr/bin/env python3

import os
import requests
import json

src_dir = "/data/feedback"
url = "http://34.132.74.9/feedback/"

for filename in os.listdir(src_dir):
    file_path = os.path.join(src_dir, filename)

    with open(file_path) as file:
        lines = file.readlines()
        entry = {"title": lines[0].strip(), "name": lines[1].strip(
        ), "date": lines[2].strip(), "feedback": "".join(lines[3:]).strip()}
        response = requests.post(url, json=entry)
