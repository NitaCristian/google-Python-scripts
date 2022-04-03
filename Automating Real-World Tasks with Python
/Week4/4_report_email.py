#!/usr/bin/env python3
import emails
import reports
import os
import datetime

src_dir = "/home/student-03-ac477d965949/supplier-data/descriptions"


def get_fruit_data():
    data = []

    for file_name in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data.append({"name": lines[0], "weight": lines[1]})

    return data


def main():
    content = get_fruit_data()
    reports.generate_report(
        "/tmp/processed.pdf", "Processed Update on {}".format(datetime.datetime.now().strftime("%B %d, %Y")), content)
    emails.send(emails.generate("automation@example.com", "{}@example.com".format(os.environ['USER']), "Upload Completed - Online Fruit Store",
                "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf"))


if __name__ == "__main__":
    main()
