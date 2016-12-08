# -*- coding: utf-8 -*-

import pprint

from ladon.clients.jsonwsp import JSONWSPClient

from lib import com_config, com_logger


class ClientWebServices:
    def __init__(self):
        conf = com_config.Config()
        config = conf.getconfig()
        self.url = config['WEBSERVICES']['url']
        
        self.logger = com_logger.Logger('Cleint WS')
    
    def print_result(self, jsonwsp_resp):
        if jsonwsp_resp.status == 200:
            if 'result' in jsonwsp_resp.response_dict:
                pprint.pprint(jsonwsp_resp.response_dict['result'], indent = 2)
            else:
                pprint.pprint(jsonwsp_resp.response_dict)
        else:
            self.logger.error('A problem occured while communicating with the service')
            self.logger.error(jsonwsp_resp.response_body)
    
    def getversion(self):
        try:
            calc_client = JSONWSPClient(self.url + '/InfoService/jsonwsp/description')
            jsonwsp_resp = calc_client.getversion()
            self.logger.debug('Call WS getversion')
            self.logger.debug(jsonwsp_resp.response_dict['result'][0]['version'])
        except Exception as exp:
            self.logger.error(repr(exp))
    
    def getlistAlbums(self):
        calc_client = JSONWSPClient(self.url + '/AlbumService/jsonwsp/description')
        jsonwsp_resp = calc_client.listAlbums(search_frase = 'Bowie')
        self.print_result(jsonwsp_resp)
    
    def getcalculator(self):
        try:
            calc_client = JSONWSPClient(self.url + '/CalculatorService/jsonwsp/description')
            jsonwsp_resp = calc_client.add(a = 25, b = 1)
            self.print_result(jsonwsp_resp)
            self.logger.debug('Call WS getcalculator')
        except Exception as exp:
            self.logger.error(repr(exp))
    
    def gettemphum(self):
        try:
            calc_client = JSONWSPClient(self.url + '/DHT22Service/jsonwsp/description')
            jsonwsp_resp = calc_client.read()
            self.print_result(jsonwsp_resp)
            self.logger.debug('Call WS getmysql')
        except Exception as exp:
            self.logger.error(repr(exp))
    
    def inserttemphum(self, temperature, humidity):
        try:
            calc_client = JSONWSPClient(self.url + '/SQLiteService/jsonwsp/description')
            jsonwsp_resp = calc_client.inserttemphum(temp = temperature, hum = humidity)
            self.print_result(jsonwsp_resp)
            self.logger.debug('Call WS getmysql')
        except Exception as exp:
            self.logger.error(repr(exp))
