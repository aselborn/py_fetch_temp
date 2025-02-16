import sqlite3
import json
import requests
import configparser

class ManageDB:

    configmanager = configparser.ConfigParser()

    def __init__(self, path):
        self.path = path
        self.configmanager.read('config.ini')

    def create_station_table(self):
        conn = sqlite3.connect(self.path)

        # create station table
        tblsql = "CREATE TABLE IF NOT EXISTS Station (StationId INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, owner INTEGER, "
        tblsql += "ownerCategory TEXT, measuringStations TEXT, id INTEGER, "
        tblsql += " height INTEGER, latitude NUMERIC, longitude NUMERIC, active INTEGER, "
        tblsql += "dtFrom TEXT, dtTo TEXT, key INTEGER, updated TEXT, title TEXT, Summary TEXT, "
        tblsql += "PRIMARY KEY(StationId AUTOINCREMENT))"

        conn.execute(tblsql)

    def create_data_table(self):
        conn = sqlite3.connect(self.path)

        tblsql ="CREATE TABLE IF NOT EXISTS Data (DataId INTEGER NOT NULL, StationId INT NOT NULL,ParameterId INT NOT NULL, PeriodId INT NOT NULL, "
        tblsql += "Temperature NUMERIC NOT NULL, DateValue INTEGER, TimeValue Integer, DateTimeValue TEXT NOT NULL,  "
        tblsql += "PRIMARY KEY (DataId AUTOINCREMENT), FOREIGN KEY (StationId) REFERENCES Stations)"

        conn.execute(tblsql)

    def create_runconfig(self):
        conn = sqlite3.connect(self.path)

        tblsql = "CREATE TABLE IF NOT EXISTS RunConfig (RunId INTEGER NOT NULL, StationId INT NOT NULL, "
        tblsql += "ParameterId INT NOT NULL, PeriodId INTEGER NOT NULL, latestHour  INTEGER NOT NULL, "
        tblsql += "latestDay INTEGER NOT NULL, latestMonths INTEGER NOT NULL, archive INTEGER NOT NULL, "
        tblsql += "PRIMARY KEY(RunId AUTOINCREMENT), FOREIGN KEY(StationId) REFERENCES  Stations)"

        conn.execute(tblsql)

    def create_periods(self):
        conn = sqlite3.connect(self.path)

        tblsql = "CREATE TABLE IF NOT EXISTS Periods (PeriodId INTEGER NOT NULL, PeriodName Text) "

        conn.execute(tblsql)

    def fetch_stations(self):
        
        headers = {'Accept':'application/json'}
        response = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json", headers=headers)
        rep = response.json()
        stationer = rep["station"]
        print("Stationer nedladdade. " )

        if not stationer is None:
            print(self.path)
            conn = sqlite3.connect(self.path)
            conn.execute("Delete from Station")

            cur = conn.cursor()

            for inp in stationer:
                sql = "INSERT INTO Station (name, owner, ownerCategory, measuringStations, id, height, latitude, longitude, active, dtfrom, dtto, key, updated, title, summary)"
                sql = sql + f' values {inp["name"], inp["owner"], inp["ownerCategory"], inp["measuringStations"], inp["id"], inp["height"], inp["latitude"], inp["longitude"], inp["active"], inp["from"], inp["to"], inp["key"], inp["updated"], inp["title"], inp["summary"]}'
                cur.execute(sql)

            conn.commit()
            conn.close()

        print("Stationer hämtade och sparade i databas.")

    def fetch_temperature(self, station, id=True):
        station_number = int (station)
        paramKey = 1
        period_name = "latest-hour"
        headers = {'Accept':'application/json'}
        response = f"{self.configmanager['smhiapi']['url']}/version/latest/parameter/{paramKey}/station/{station_number}/period/{period_name}/data.json"
        print(response)
        # response = config.smhiApi 
        # response = databaseConfig.SmhiApi, "/version/latest/parameter/", paramKey, "/station/", "[stationKey]", "/period/", "[periodName]", "/data.json");
        response = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json", headers=headers)
        rep = response.json()
        print (rep)



