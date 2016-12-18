"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : //2017
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from lib.driver.oled.demo_opts import device
from lib.driver.oled.virtual import viewport
from lib.driver.oled.render import canvas
from PIL import Image
import os, time
import datetime

dayofweek = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']


blurb = """


   Episode IV:
   A NEW HOPE

It is a period of
civil war. Rebel
spaceships, striking
from a hidden base,
have won their first
victory against the
evil Galactic Empire.

During the battle,
Rebel spies managed
to steal secret plans
to the Empire's ulti-
mate weapon, the
DEATH STAR, an armor-
ed space station with
enough power to des-
troy an entire planet.

Pursued by the
Empire's sinister
agents, Princess Leia
races home aboard her
starship, custodian
of the stolen plans
that can save her
people and restore
freedom to the
galaxy....
"""


def main():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'starwars.png'))
    logo = Image.open(img_path)

    virtual = viewport(device, width=128, height=768)

    for _ in range(2):
        with canvas(virtual) as draw:
            draw.text((0, 0), "A long time ago", fill="white")
            draw.text((0, 12), "in a galaxy far", fill="white")
            draw.text((0, 24), "far away....", fill="white")

    time.sleep(5)

    for _ in range(2):
        with canvas(virtual) as draw:
            draw.bitmap((20, 0), logo, fill="white")
            for i, line in enumerate(blurb.split("\n")):
                draw.text((0, 40 + (i * 12)), text=line, fill="white")

    time.sleep(2)

    # update the viewport one position below, causing a refresh,
    # giving a rolling up scroll effect when done repeatedly
    for y in range(450):
        virtual.set_position((0, y))
        time.sleep(0.01)


if __name__ == "__main__":
    try:
        date = datetime.datetime.now()
        print(dayofweek[date.weekday()])
        print(str(date.day) + '/' + str(date.month) + '/' + str(date.year))
        print(str(date.hour) + ':' + str(date.minute) + ':' + str(date.second))
        # main()
    except KeyboardInterrupt:
        pass
