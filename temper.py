import sqlite3
import sys, os 
import getopt
import json
import requests
import sqlite3

# database_file = "C:/Users/nrobl/source/repos/tmpimport/db/Temperature.db"
database_file = os.getcwd() + "\DbTemperatur.db"

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
    rep = response.json()
    stationer = rep["station"]
    print("Stationer nedladdade. " )
    return stationer

def spara_stationer(stationer):
    if not stationer is None:
        print(database_file)


        conn = sqlite3.connect(database_file)

        
        cur = conn.cursor()

        for inp in stationer:
            sql = "INSERT INTO Station (name, owner, ownerCategory, measuringStations, id, height, latitude, longitude, active, dtfrom, dtto, key, updated, title, summary)"
            sql = sql + f' values {inp["name"], inp["owner"], inp["ownerCategory"], inp["measuringStations"], inp["id"], inp["height"], inp["latitude"], inp["longitude"], inp["active"], inp["from"], inp["to"], inp["key"], inp["updated"], inp["title"], inp["summary"]}'
            print(sql)
            cur.execute(sql)

        conn.commit()
        conn.close()

if __name__ == '__main__':
    main()
    stationer = download_stations()
    spara_stationer(stationer)
    

