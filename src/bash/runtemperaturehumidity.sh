#!/bin/sh

cd /home/project/TemperatureHumidityServer
pigpiod
python3.4 main.py
pkill pigpiod
