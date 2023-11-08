import pandas as pd
import csv
import re

def run_function():

    # Open a CSV file for reading
    with open('resources/minute_values.csv', newline='') as csvfile:
        
        #In Python, a CSV dialect refers to a set of rules and conventions that define the format of a Comma-Separated Values (CSV) file. 
        #These rules include specifications for delimiters, quoting characters, escape characters, and more, 
        # which determine how the data within the CSV file is structured and how special characters are handled.
        devices = csvfile.readline()
        dialect=csv.Sniffer().sniff(devices)

        devices = devices.split(";")
        measures = csvfile.readline().split(";")
        headers = ['Timestamp']
        
        for x in range(1, len(measures)):
            device = devices[x] if devices[x] != '""' else device
            device = device.replace('"', '') 
            
            head = measures[x]
            head = head.replace('"', '')

            headers.append(device + ':' + head) 
        

        # Create a DictReader object
        reader = csv.DictReader(csvfile, dialect=dialect, fieldnames=headers)
        #n = 0
        #for row in reader:
            #if n == 2: exit() 
            #else: n += 1 

            #print(row, end="\n\n")
            #print(row['Sensor: S 1 (#1, 63):Irradiation (W/m2)'], end="\n\n")
