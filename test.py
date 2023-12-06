import pandas as pd
import csv
import re

class X:
    def __init__(self, id, name, age, height):
        self.id = id
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"id: {self.id} name: {self.name} age: {self.age}  height: {self.height}"


class Y:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"id: {self.id} name: {self.name} age: {self.age}"


# if __name__ == '__main__':
#     x = X(1, "ola", 3, 10)
#     y = Y(2, "xau", 5)
#
#     for k, v in x.__dict__.items():
#         if hasattr(y, k):
#             setattr(y, k, v)
#
#     print(y.__dict__)


def run_function():
    # Open a CSV file for reading
    with open('resources/farm_data/quinta/minute_values.csv', newline='') as csvfile:
        # In Python, a CSV dialect refers to a set of rules and conventions that define the format of a Comma-Separated Values (CSV) file.
        # These rules include specifications for delimiters, quoting characters, escape characters, and more,
        # which determine how the data within the CSV file is structured and how special characters are handled.
        devices = csvfile.readline()
        dialect = csv.Sniffer().sniff(devices)

        devices = devices.split(";")
        measures = csvfile.readline().split(";")
        headers = ['Timestamp']

        for x in range(1, len(measures)):
            device = devices[x] if devices[x] != '""' else device
            device = device.replace('"', '')

            head = measures[x]
            head = head.replace('"', '')

            headers.append(device + ';' + head)

            # Create a DictReader object
        reader = csv.DictReader(csvfile, dialect=dialect, fieldnames=headers)

        n = 0
        for row in reader:

            for k, v in row.items():
                if k == 'Timestamp':
                    print(v)

            if n == 1:
                exit()
            n += 1

            # print(row, end="\n\n")
            # print(row['Sensor: S 1 (#1, 63):Irradiation (W/m2)'], end="\n\n")


if __name__ == '__main__':
    run_function()
