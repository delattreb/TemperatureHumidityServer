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
        self.lcd.rectangle(0, 0, self.lcd.width_max - 1, 45)
        self.lcd.text(2, 3, self.config['APPLICATION']['name'], 1)
        self.lcd.text(5, 18, 'v' + self.config['APPLICATION']['version'], 0)
        self.lcd.text(5, 32, self.config['APPLICATION']['author'], 0)
        
        for i in range(19):
            self.lcd.progessbar(0, 53, 127, 10, i, 18, 5, 2, 4, True)
            self.lcd.display()
            time.sleep(0.35)
    
    def progressbarreadoff(self):
        self.lcd.rectangleclear(0, 3, 8, 61)
    
    def progressbarwsoff(self):
        self.lcd.rectangleclear(12, 3, 8, 61)
    
    def displaysensor(self, temp, hum, cptread, delayread, cptws, delayws):
        # Erase
        self.lcd.rectangleclear(60, 4, 62, 24)
        self.lcd.rectangleclear(60, 41, 65, 22)
        
        # DHT22
        self.lcd.text(25, 2, 'Temp', 0)
        self.lcd.text(60, 1, str(temp)[:4], 2)
        self.lcd.text(117, 1, '°', 1)
        
        self.lcd.text(25, 37, 'Hum', 0)
        self.lcd.text(60, 38, str(hum)[:4], 2)
        self.lcd.text(115, 51, '%', 1)
        
        # Draw Line
        self.lcd.line(55, 0, 55, 63, 1)
        self.lcd.line(55, 35, 127, 35, 1)
        # self.lcd.line(23, 0, 23, 63, 1)
        
        # Draw progressbar
        self.lcd.line(1, 4, 7, 4, 1)
        self.lcd.line(13, 4, 19, 4, 1)
        self.lcd.progessbar(0, 3, 8, 61, cptread, delayread, 8, 2, 0, False)
        self.lcd.progessbar(12, 3, 8, 61, cptws, delayws, 8, 2, 0, False)
        
        # self.lcd.progessbar(0, 10, 121, 10, 100, 100, 8, 2, 0, False)
        
        self.lcd.display()
