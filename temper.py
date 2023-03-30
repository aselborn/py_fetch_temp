import sqlite3
import sys
import getopt
import json
import requests

database_file = "C:/Users/nrobl/source/repos/tmpimport/db/Temperature.db"
dataFil = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/52230/period/latest-months/data.csv"


def main():
    d = sys.getwindowsversion()
    print(d)


def print_info():
    print("Ge temper.py --smhi")


def connect_mysql():
    print("hej")


def download():
    # req = urllib.request.Request(dataFil)
    headers = {'Accept':'application/json'}
    response = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest.json", headers=headers)
    data = response.json()
    print("ok")

def download_stations():
    headers = {'Accept':'application/json'}
    response = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json", headers=headers)
    data = response.json()
    print("ok")


if __name__ == '__main__':
    main()
    # download()
    download_stations()
