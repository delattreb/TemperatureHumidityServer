#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import time

from PIL import Image
from demo_opts import device
from oled.render import canvas

with canvas(device) as draw:
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'pi_logo.png'))
    logo = Image.open(img_path)
    draw.bitmap((32, 0), logo, fill = "white")

try:
    time.sleep(5)
except KeyboardInterrupt:
    pass
