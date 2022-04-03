# import csv

# # csv_file = "persoane.csv"
# # entries = []
# # with open(csv_file) as file:
# #     rows = csv.DictReader(file)
# #     for row in rows:
# #         entries.append(row)

# #     csv_file_output = "persoane_copy.csv"
# #     with open(csv_file_output, 'w', newline='') as file:
# #         field_names = ["Nume", "Email"]
# #         writer = csv.DictWriter(file, field_names)
# #         writer.writeheader()
# #         writer.writerows(entries)


# csv_file = "persoane.csv"
# entries = []
# with open(csv_file) as file:
#     rows = csv.reader(file)
#     for index, row in enumerate(rows):
#         print(index, row)

import pandas
df = pandas.read_csv('persoane.csv')
print(df)
print(df["Nume"][0])