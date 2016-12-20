"""
main.py v 1.1.5
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import threading

from acquisition import thread_acquisition_dht22
from lib import com_config, com_lcd, com_logger
from lib.driver import com_gpio_inout

# Config
conf = com_config.Config()
conf.setconfig()
config = conf.getconfig()

# Log
logger = com_logger.Logger()
logger.info('Application start')

# LCD
lcd = com_lcd.LCD()

# LCD Splash (not display if debug mode)
if int(config['LOGGER']['levelconsole']) > 10:
    logger.info('Splash screen')
    lcd.splash()

# Create new threads
threadlock = threading.Lock()

# TODO : Start pigpiod
dht22_thread_int = thread_acquisition_dht22.ThreadAcquisitionDHT22(config['GPIO']['DHT22_INTERIOR_NAME'], threadlock, int(config['GPIO']['DHT22_INTERIOR_PORT']), int(config['GPIO']['DHT22_INTERIOR_delay']),
                                                                   int(config['GPIO']['DHT22_INTERIOR_delayread']), int(config['GPIO']['DHT22_INTERIOR_delayws']), int(config['GPIO']['DHT22_INTERIOR_nb']),
                                                                   int(config['GPIO']['LED_ACQUISITION']), True)
dht22_thread_int.start()

# Wait end for each thread
dht22_thread_int.join()

# logger.info('Application stop')
gpio = com_gpio_inout.GPIOINOT()
gpio.cleanup()
