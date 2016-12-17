#!/bin/sh

cd /home/project/TemperatureHumidityServer
cp database.db databasecopy.db
python3.4 runexportdata.py
rm databasecopy.db
