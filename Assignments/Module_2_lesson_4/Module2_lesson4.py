# Practising to write dictionary to csv

big_list = [
    {"name": "Fredrick Stein", "userid": 6712359021, "is_admin": False},
    {"name": "Wiltmore Denis", "userid": 2525942, "is_admin": False},
    {"name": "Greely Plonk", "userid": 158990235, "is_admin": False},
    {"name": "Dendris Stulo", "userid": 572189563, "is_admin": True}]

import csv

with open("output.csv", "w") as outpujt_csv:
    fields = ["name", "userid", "is_admin"]
    output_writer = csv.DictWriter(outpujt_csv, fieldnames=fields)
    output_writer.writeheader()

    for item in big_list:
        output_writer.writerow(item)