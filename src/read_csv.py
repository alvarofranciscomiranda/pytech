import pandas as pd
import csv
import re

def run_function():

    with open('resources/minute_values.csv', newline='') as csvfile:
        
        devices = csvfile.readline()
        dialect=csv.Sniffer().sniff(devices)

        devices = devices.split(";")
        variables = csvfile.readline().split(";")
        headers = []
        for x in range(1, len(variables)):
            device = devices[x] if devices[x] != '""' else device 

            head = variables[x]

            headers.append(device + head)

        #header = csvfile.readline()

        reader = csv.DictReader(csvfile, dialect=dialect, fieldnames=headers)
        
        print(devices, end="\n\n")
        for row in reader:
            print(row.keys(), end="\n\n")
            print(row, end="\n\n")

            exit()

    # Now, data_dict contains the organized data
    #print_value = data_dict["Inverter 1"]["2023-09-01 00:00:00"]["Pac (W)"]

    #print(print_value)