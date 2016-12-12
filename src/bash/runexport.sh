#!/bin/sh

cd /volume1/web/temperaturehumidityserver
cp database.db databasecopy.db
python3.5 runexportdata.py
rm databasecopy.db
