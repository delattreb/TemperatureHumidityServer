# -*- coding: utf-8 -*-
import wsgiref.simple_server
from os.path import abspath, dirname, join, normpath

from ladon.server.wsgi import LadonWSGIApplication
from ladon.tools.log import set_log_backup_count, set_log_maxsize, set_logfile, set_loglevel

from lib import com_config, com_logger


class ServerWebServices:
    def __init__(self):
        self.logger = com_logger.Logger('Server WS')
        conf = com_config.Config()
        self.config = conf.getconfig()
        
        # Log server WebServices
        set_logfile(join(dirname(normpath(abspath(__file__))), self.config['WEBSERVICES']['logfile']))
        set_loglevel(int(self.config['WEBSERVICES']['loglevel']))
        set_log_backup_count(int(self.config['WEBSERVICES']['logbackupcount']))
        set_log_maxsize(int(self.config['WEBSERVICES']['logfilesize']))
    
    def run(self):
        port = int(self.config['WEBSERVICES']['port'])
        self.logger.info('Services are running on port %(port)s.' % {'port': port})
        # Set list of WebServices
        scriptdir = dirname(abspath(__file__))
        service_modules = ['infoservice', 'sqliteservice']
        application = LadonWSGIApplication(service_modules, [join(scriptdir, 'services')], catalog_name = self.config['WEBSERVICES']['name'],
                                           catalog_desc = self.config['WEBSERVICES']['description'], logging = 31)
        
        server = wsgiref.simple_server.make_server('', port, application)
        server.serve_forever()
