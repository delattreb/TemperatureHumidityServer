"""
lcd.py v1.0.0
Auteur: Bruno DELATTRE
Date : 13/11/2016
"""

import math
import os

from PIL import ImageFont

from lib import com_config
from oled.demo_opts import device
from oled.render import canvas


class LCD:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'FreeSans.ttf'))
        self.smallfont = ImageFont.truetype(font_path, 10)
        self.normalfont = ImageFont.truetype(font_path, 14)
        self.bigfont = ImageFont.truetype(font_path, 27)
    
    def splash(self, duration):
        i = 0
        while i <= 127:
            with canvas(device) as draw:
                # with canvas(device) as draw:
                draw.rectangle((0, 0, device.width - 1, 45), fill = 0, outline = 1)
                draw.text((4, 3), self.config['APPLICATION']['name'], fill = "white")
                draw.text((5, 18), 'v' + self.config['APPLICATION']['version'], fill = "white")
                draw.text((5, 32), self.config['APPLICATION']['author'], fill = "white")
                self.progressbarline(draw, 0, 53, 127, 10, i, 127, 2)
            i += 1
    
    def progressbarline(self, draw, x, y, width, height, value, max_value, interior = 2):
        # with canvas(device) as draw:
        interiormini = interior / 2
        
        # Exterior progressbar
        draw.rectangle((x, y, x + width, y + height), outline = 1, fill = 0)
        
        # Interior
        # Horizontal or vertical
        if width > height:  # Horizontal
            cal = round((((width - interior) * value) / max_value), 0)
            draw.rectangle((x + interiormini, y + interiormini, x + interiormini + cal, y + height - interiormini), outline = 0, fill = 1)
        else:  # Vertical
            cal = round((((height - interior) * value) / max_value), 0)
            draw.rectangle((x + interiormini, y + height - interiormini, x + width - interiormini, y + (height - cal) - interiormini), outline = 0, fill = 1)
    
    def progressbar(self, draw, x, y, width, height, value, max_value, thickness, space, interior = 2, border = True):
        interiormini = interior / 2
        
        # Exterior progressbar
        if border:
            draw.rectangle((x, y, x + width, y + height), outline = 1, fill = 0)
        
        # Interior
        # Horizontal or vertical
        if width > height:  # Horizontal
            totalblock = round((width - interior) / (thickness + space), 0)
            cal = int(round(((totalblock * value) / max_value), 0))
            index = x + interiormini
            for i in range(0, cal):
                draw.rectangle((index, y + interiormini, index + thickness, y + height - interiormini), outline = 0, fill = 1)
                index += (thickness + space)
        else:  # Vertical
            totalblock = round((height - interior) / (thickness + space), 0)
            cal = int(round(((totalblock * value) / max_value), 0))
            index = y + height - interiormini
            for i in range(0, cal):
                draw.rectangle((x + interiormini, index, x + width - interiormini, index - thickness), outline = 0, fill = 1)
                index -= (thickness + space)
    
    def progresscircle(self, draw, x, y, radius, thickness, maxsegments, segments, startangle, totalangle, direction):
        anglechange = (totalangle / maxsegments) * (math.pi / 180)
        i = startangle * (math.pi / 180)
        
        ax = x + (math.cos(i) * radius)
        ay = y - (math.sin(i) * radius)
        
        bx = x + (math.cos(i) * (radius + thickness))
        by = y - (math.sin(i) * (radius + thickness))
        
        for cpt in range(segments):  # for optimisation last process cpt is last value to segments new value
            i += direction * anglechange
            
            cx = x + (math.cos(i) * radius)
            cy = y - (math.sin(i) * radius)
            
            dx = x + (math.cos(i) * (radius + thickness))
            dy = y - (math.sin(i) * (radius + thickness))
            
            # TODO one only
            draw.polygon((ax, ay, bx, by, dx, dy), fill = 1, outline = 1)  # Color 1
            # self.oled.surface.polygon((ax, ay, cx, cy, dx, dy), fill = 1, outline = 1)  # Color 2
            
            ax = cx
            ay = cy
            
            bx = dx
            by = dy
    
    def displaysensor(self, temp, hum, cptread, delayread, cptws, delayws):
        with canvas(device) as draw:
            # DHT22
            draw.text((25, 16), 'Temp', fill = "white", font = self.smallfont)
            draw.text((60, 1), str(temp)[:4], fill = "white", font = self.bigfont)
            draw.text((117, 1), '°', fill = "white", font = self.normalfont)
            
            draw.text((25, 52), 'Hum', fill = "white", font = self.smallfont)
            draw.text((60, 38), str(hum)[:4], fill = "white", font = self.bigfont)
            draw.text((115, 47), '%', fill = "white", font = self.normalfont)
            
            # Draw Line
            draw.line((55, 0, 55, 63), 1)
            draw.line((55, 35, 127, 35), 1)
            # self.lcd.line(23, 0, 23, 63, 1)
            
            # Draw progressbar
            draw.line((1, 4, 7, 4), 1)
            draw.line((13, 4, 19, 4), 1)
            
            self.progressbar(draw, 0, 3, 8, 61, cptread, delayread, 8, 2, 0, False)
            self.progressbar(draw, 12, 3, 8, 61, cptws, delayws, 8, 2, 0, False)
