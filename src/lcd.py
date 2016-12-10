"""
lcd.py v1.0.0
Auteur: Bruno DELATTRE
Date : 13/11/2016
"""

import time

from lib import com_config, com_ssd1306


class LCD:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.lcd = com_ssd1306.SSD1306()
    
    def displayoff(self):
        self.lcd.offscreen()
    
    def splash(self, duration):
        self.lcd.clear()
        self.lcd.rectangle(0, 0, self.lcd.width_max - 1, self.lcd.height_max - 1)
        self.lcd.text(2, 3, self.config['APPLICATION']['name'], 1)
        self.lcd.text(7, 21, 'v' + self.config['APPLICATION']['version'], 1)
        self.lcd.text(4, 48, self.config['APPLICATION']['author'], 0)
        
        self.lcd.display()
        time.sleep(duration)
    
    def displaysensor(self, temp, hum):
        self.lcd.clear()
        # DHT22
        self.lcd.text(1, 5, 'Temp', 0)
        self.lcd.text(40, 1, str(temp), 2)
        self.lcd.text(97, 1, '°', 1)
        
        self.lcd.text(1, 43, 'Hum', 0)
        self.lcd.text(40, 38, str(hum), 2)
        self.lcd.text(99, 51, '%', 1)
        
        self.lcd.line(33, 1, 33, 64, 1)
        self.lcd.line(33, 36, 127, 36, 1)
        
        self.lcd.display()
