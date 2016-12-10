#!/bin/sh

cd /volume1/web/TemperatureHumidityServer
cp database.db databasecopy.db
python3.5 runexportdata.py
rm databasecopy.db
