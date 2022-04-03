#!/usr/bin/env python3
import shutil
import psutil
import subprocess
import emails
import os


def check_cpu():
    if psutil.cpu_percent() > 80:
        return "Error - CPU usage is over 80%"
    return None


def check_disk():
    total, used, free = shutil.disk_usage('/')
    free_percent = round(free / total * 100)
    if free_percent < 20:
        return "Error - Available disk space is less than 20%"
    return None


def check_memory():
    memory = dict(psutil.virtual_memory()._asdict())
    available_memory = memory["available"] >> 20
    if available_memory < 500:
        return "Error - Available memory is less than 500MB"
    return None


def check_hostname():
    result = subprocess.run(["host", "localhost"], capture_output=True)
    if result.returncode != 0:
        return "Error - localhost cannot be resolved to 127.0.0.1"
    return None


def main():
    list_errors = [check_cpu(), check_disk(), check_memory(), check_hostname()]
    for error in list_errors:
        if error != None:
            emails.send(emails.generate_error_report("automation@example.com", "{}@example.com".format(
                os.environ['USER']), error, "Please check your system and resolve the issue as soon as possible."))
            break


if __name__ == "__main__":
    main()
