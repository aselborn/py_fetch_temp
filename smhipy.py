import csv
import os
import sys
import time

csv_file = 'd.csv'


def file_parser(fil):
    print(fil)
    with open(fil, 'r') as f:
        contents = f.read()
    print(contents)


def parse_csv(fil):
    begin_read = False
    with open(fil) as data_csv_file:
        read_csv = csv.reader(data_csv_file, delimiter=';')

        line_count = 0
        for row in read_csv:
            print(row)


if __name__ == "__main__":
    parse_csv(csv_file)

