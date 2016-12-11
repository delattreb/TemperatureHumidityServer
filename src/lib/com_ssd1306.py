"""
com_lcd.py v1.0.2
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

from PIL import ImageFont

from lib import com_logger
from lib.com_ssd1306I2C import ssd1306I2C

try:
    from smbus import SMBus
except:
    SMBus=None


def is_plugged(function):
    def plugged(*original_args, **original_kwargs):
        return function(*original_args, **original_kwargs)
    
    if not SMBus:
        logger=com_logger.Logger('LCD')
        logger.warning('LCD not present')
    
    return plugged


class SSD1306:
    @is_plugged
    def __init__(self):
        # Constant
        self.SMALL_FONT=0
        self.DEFAULT_FONT=1
        self.STRONG_FONT=2
        
        # Font
        self.__smallFont=ImageFont.truetype('font/FreeSans.ttf', 11)
        self.__defaultFont=ImageFont.truetype('font/FreeSans.ttf', 13)
        self.__bigFont=ImageFont.truetype('font/FreeSans.ttf', 29)
        
        self.oled=ssd1306I2C(SMBus(1)) if SMBus is not None else None
        self.width_max=self.oled.width if SMBus is not None else 0
        self.height_max=self.oled.height if SMBus is not None else 0
    
    def display(self):
        if SMBus is not None:
            self.oled.display()
    
    def offscreen(self):
        if SMBus is not None:
            self.oled.onoff(0)
    
    def clear(self):
        if SMBus is not None:
            self.oled.cls()
    
    def text(self, x, y, text, fontHeight):
        if SMBus is not None:
            draw=self.oled.canvas
            if fontHeight == self.SMALL_FONT:
                draw.text((x, y), text, font=self.__smallFont, fill=1)
            
            if fontHeight == self.DEFAULT_FONT:
                draw.text((x, y), text, font=self.__defaultFont, fill=1)
            
            if fontHeight == self.STRONG_FONT:
                draw.text((x, y), text, font=self.__bigFont, fill=1)
    
    def rectangle(self, x, y, width, height):
        if SMBus is not None:
            self.oled.canvas.rectangle((x, y, x+width, y+height), outline=1, fill=0)
    
    def rectangleclear(self, x, y, width, height):
        if SMBus is not None:
            self.oled.canvas.rectangle((x, y, x+width, y+height), outline=0, fill=0)
    
    def line(self, x1, y1, x2, y2, width):
        if SMBus is not None:
            self.oled.canvas.line((x1, y1, x2, y2), fill=1, width=width)
    
    def progressbarline(self, x, y, width, height, value, max_value, interior=2):
        if SMBus is not None:
            
            # Exterior progressbar
            self.oled.canvas.rectangle((x, y, x+width, y+height), outline=1, fill=0)
            
            # Interior
            # Horizontal or vertical
            if width>height:  # Horizontal
                cal=round((((width-interior)*value)/max_value), 0)
                self.oled.canvas.rectangle(
                    (x+(interior/2), y+(interior/2), x+(interior/2)+cal, y+height-(interior/2)),
                    outline=0, fill=1)
            else:  # Vertical
                cal=round((((height-interior)*value)/max_value), 0)
                self.oled.canvas.rectangle(
                    (x+(interior/2), y+height-(interior/2), x+width-(interior/2), y+(height-cal)-(interior/2)),
                    outline=0, fill=1)
    
    def progessbar(self, x, y, width, height, value, max_value, thickness, space, interior=2, border=True):
        if SMBus is not None:
            # block count
            # block=round((height-interior)/(thickness+space), 0)
            
            # Exterior progressbar
            if border:
                self.oled.canvas.rectangle((x, y, x+width, y+height), outline=1, fill=0)
            
            # Interior
            # Horizontal or vertical
            if width>height:  # Horizontal
                totalblock=round((width-interior)/(thickness+space), 0)
                cal=int(round(((totalblock*value)/max_value), 0))
                index=x+(interior/2)
                for i in range(0, cal):
                    self.oled.canvas.rectangle(
                        (index, y+(interior/2), index+thickness, y+height-(interior/2)),
                        outline=0, fill=1)
                    index+=(thickness+space)
            else:  # Vertical
                totalblock=round((height-interior)/(thickness+space), 0)
                cal=int(round(((totalblock*value)/max_value), 0))
                index=y+height-(interior/2)
                for i in range(0, cal):
                    self.oled.canvas.rectangle(
                        (x+(interior/2), index, x+width-(interior/2), index-thickness),
                        outline=0, fill=1)
                    index-=(thickness+space)
