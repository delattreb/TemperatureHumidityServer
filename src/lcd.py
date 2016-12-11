"""
lcd.py v1.0.0
Auteur: Bruno DELATTRE
Date : 13/11/2016
"""

import time

from lib import com_config, com_ssd1306


class LCD:
    def __init__(self):
        conf=com_config.Config()
        self.config=conf.getconfig()
        self.lcd=com_ssd1306.SSD1306()
    
    def displayoff(self):
        self.lcd.offscreen()
    
    def splash(self, duration):
        self.lcd.clear()
        self.lcd.rectangle(0, 0, self.lcd.width_max-1, self.lcd.height_max-1)
        self.lcd.text(2, 3, self.config['APPLICATION']['name'], 1)
        self.lcd.text(7, 21, 'v'+self.config['APPLICATION']['version'], 1)
        self.lcd.text(4, 48, self.config['APPLICATION']['author'], 0)
        
        self.lcd.display()
        time.sleep(duration)
    
    def displaysensor(self, temp, hum):
        # Erase
        self.lcd.rectangleclear(46, 4, 62, 25) # TODO a revoir
        self.lcd.rectangleclear(46, 40, 68, 23) # TODO a revoir
        
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
        
        # Draw progressbar
        self.lcd.progessbar(0, 0, 10, 63, 100, 100, 4)

        #self.lcd.progessbar(0, 10, 127, 10, 50, 100, 4)

        self.lcd.display()
