#!/bin/sh

cd /home/project/TemperatureHumidityServer/src/
pigpiod
python3.4 main.py
pkill pigpiod
