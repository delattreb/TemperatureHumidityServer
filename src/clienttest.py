# -*- coding: utf-8 -*-

import os
import pprint
from os.path import abspath, dirname, join

from ladon.clients.jsonwsp import JSONWSPClient

base_url = 'http://192.168.1.15:9090'

files_dir = join(dirname(abspath(__file__)), 'files')
download_dir = join(dirname(abspath(__file__)), 'download')

for d in [files_dir, download_dir]:
    if not os.path.exists(d):
        os.mkdir(d)


def print_result(jsonwsp_resp):
    if jsonwsp_resp.status == 200:
        if 'result' in jsonwsp_resp.response_dict:
            pprint.pprint(jsonwsp_resp.response_dict['result'], indent = 2)
        else:
            pprint.pprint(jsonwsp_resp.response_dict)
    else:
        print("A problem occured while communicating with the service:\n")
        print(jsonwsp_resp.response_body)


def testAlbumService():
    print("\n\nTesting AlbumService:\n")
    # Load the AlbumService description
    album_client = JSONWSPClient(base_url + '/AlbumService/jsonwsp/description')
    
    # Fetch albums containing the substring "Zoo" in the album title
    jsonwsp_resp = album_client.listAlbums(search_frase = 'Bowie')
    print_result(jsonwsp_resp)
    
    # Fetch all bands containing the substring "Bowie" in the band name
    jsonwsp_resp = album_client.listBands(search_frase = 'Bowie')
    print_result(jsonwsp_resp)


testAlbumService()
