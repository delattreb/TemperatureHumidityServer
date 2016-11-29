"""
main.py v 1.1.5
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import threading
import lcd
from lib import com_config, com_gpio_inout, com_logger
from acquisition import thread_acquisition_dht22, thread_acquisition_ds18b20

# Config
com_config.setConfig()
config = com_config.getConfig()

# Log
logger = com_logger.Logger()
logger.info('Application start')

# LCD
lcd = lcd.LCD()

# LCD Splash
lcd.splash(int(config['APPLICATION']['splashduration']))

gpioinout = com_gpio_inout.GPIOINOT()
gpioinout.blink(0.2, 10)

# Create new threads
threadlock = threading.Lock()

ds18b20_thread_int = thread_acquisition_ds18b20.ThreadAcquisitionDS18B20('DS18B20 Ext', threadlock, config['GPIO']['DS18B20_1'], float(config['GPIO'][
                                                                                                                                           'DS18B20_1_delay']),
                                                                         int(config['GPIO']['DS18B20_1_nb']))

# TODO Lance pigiopd pour lire le capteur DHT22
dht22_thread_int = thread_acquisition_dht22.ThreadAcquisitionDHT22('Interior', threadlock,
                                                                   int(config['GPIO']['DHT22_INTERIOR_PORT']), int(config['GPIO']['DHT22_INTERIOR_delay']),
                                                                   int(config['GPIO']['DHT22_INTERIOR_nb']))

ds18b20_thread_int.start()
dht22_thread_int.start()

# Wait end for each thread
# ds18b20_thread_int.join()
# dht22_thread_int.join()()


logger.info('Application stop')
gpio = com_gpio_inout.GPIOINOT()
gpio.cleanup()