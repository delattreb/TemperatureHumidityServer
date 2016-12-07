# -*- coding: utf-8 -*-

import pprint

from ladon.clients.jsonwsp import JSONWSPClient

from lib import com_config, com_logger


class ClientWebServices:
    def __init__(self):
        conf = com_config.Config()
        config = conf.getconfig()
        self.url = config['WEBSERVICES']['url']
        
        self.logger = com_logger.Logger()
    
    def print_result(self, jsonwsp_resp):
        if jsonwsp_resp.status == 200:
            if 'result' in jsonwsp_resp.response_dict:
                pprint.pprint(jsonwsp_resp.response_dict['result'], indent = 2)
            else:
                pprint.pprint(jsonwsp_resp.response_dict)
        else:
            self.logger.error('A problem occured while communicating with the service')
            self.logger.error(jsonwsp_resp.response_body)
    
    def getcalculator(self, ):
        calc_client = JSONWSPClient(self.url + '/Calculator/jsonwsp/description')
        jsonwsp_resp = calc_client.add(a = 25, b = 1)
        self.print_result(jsonwsp_resp)
    
    def getmysql(self, ):
        calc_client = JSONWSPClient(self.url + '/MySQL/jsonwsp/description')
        jsonwsp_resp = calc_client.add(a = 16, b = 2)
        self.print_result(jsonwsp_resp)
