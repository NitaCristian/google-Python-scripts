import operator
import re
import csv

error = {}
per_user = {}

with open('syslog.log') as file:
    for line in file:
        result = re.search(r"ticky: ERROR ([\w ']*)\(([\w .]+)\)", line)
        if result is not None:
            error[result[1].strip()] = error.get(result[1].strip(), 0) + 1
            per_user[result[2]] = per_user.get(result[2], [0, 0])
            per_user[result[2]][1] += 1

        result = re.search(r"ticky: INFO .*\(([\w\.]*)\)", line)
        if result is not None:
            per_user[result[1]] = per_user.get(result[1], [0, 0])
            per_user[result[1]][0] += 1

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
with open('error_message.csv', 'w', newline='') as file:
    error.insert(0, ("Error", "Count"))
    writer = csv.writer(file)
    writer.writerows(error)

per_user = sorted(per_user.items(), key=operator.itemgetter(0))
with open('user_statistics.csv', 'w', newline='') as file:
    per_user.insert(0, ("Username", "INFO", "ERROR"))
    writer = csv.writer(file)
    writer.writerow(per_user[0])
    for item in per_user[1:]:
        writer.writerow((item[0], item[1][0], item[1][1]))


# ./csv_to_html.py error_message.csv /var/www/html/error_message.html
# ./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
