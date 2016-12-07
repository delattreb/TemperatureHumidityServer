# -*- coding: utf-8 -*-
import wsgiref.simple_server
from os.path import abspath, dirname, join, normpath

from ladon.server.wsgi import LadonWSGIApplication
from ladon.tools.log import set_log_backup_count, set_log_maxsize, set_logfile, set_loglevel

from lib import com_config, com_logger


class ServerWebServices:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.logger = com_logger.Logger()
        
        # Log server WebServices
        set_logfile(join(dirname(normpath(abspath(__file__))), 'webservices.log'))
        set_loglevel(4)
        set_log_backup_count(50)
        set_log_maxsize(50000)
    
    def run(self):
        port = self.config['WEBSERVICES']['port']
        
        # Set list of WebServices
        scriptdir = dirname(abspath(__file__))
        service_modules = ['calculator', 'mysql']
        application = LadonWSGIApplication(service_modules, [join(scriptdir, 'services')], catalog_name = 'MySQL WebServices',
                                           catalog_desc = 'MySQL WebServices', logging = 31)
        server = wsgiref.simple_server.make_server('', port, application)
        server.serve_forever()
        self.logger.info('Services are running on port %(port)s.' % {'port': port})
