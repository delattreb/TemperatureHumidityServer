# -*- coding: utf-8 -*-

from ladon.clients.jsonwsp import JSONWSPClient

from lib import com_config, com_logger


class ClientWebServices:
    def __init__(self):
        conf = com_config.Config()
        config = conf.getconfig()
        self.url = config['WEBSERVICES']['url']
        
        self.logger = com_logger.Logger('Cleint WS')

    def getlistAlbums(self):
        calc_client = JSONWSPClient(self.url + '/AlbumService/jsonwsp/description')
        jsonwsp_resp = calc_client.listAlbums(search_frase = 'Bowie')
        self.print_result(jsonwsp_resp)
        
    def getversion(self):
        try:
            client = JSONWSPClient(self.url + '/InfoService/jsonwsp/description')
            jsonwsp_resp = client.getversion()
            self.logger.debug('WebServices-'+client.path)
            self.logger.debug(jsonwsp_resp.response_dict['result'][0]['version'])
        except Exception as exp:
            self.logger.error(repr(exp))
    
    def inserttemphum(self, temperature, humidity):
        try:
            client = JSONWSPClient(self.url + '/SQLiteService/jsonwsp/description')
            jsonwsp_resp = client.inserttemphum(temp = temperature, hum = humidity)
            self.logger.debug('WebServices-'+client.path)
        except Exception as exp:
            self.logger.error(repr(exp))
