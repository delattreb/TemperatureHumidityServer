# -*- coding: utf-8 -*-
import pickle
from os.path import abspath, dirname, join

from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType

f = open(join(dirname(abspath(__file__)), 'albums.pickle'), 'rb')
albums = pickle.loads(f.read())
f.close()


class Band(LadonType):
    def __init__(self):
        super().__init__()
        self.name = 'bla'
    
    name = PORTABLE_STRING
    album_titles = [PORTABLE_STRING]


class Album(LadonType):
    title = PORTABLE_STRING
    songs = [PORTABLE_STRING]


class AlbumService(object):
    @ladonize(PORTABLE_STRING, rtype = [Album])
    def listAlbums(self, search_frase = PORTABLE_STRING('')):
        global albums
        album_list = []
        for band_name, albums_dict in albums.items():
            b = Band()
            b.name = band_name
            b.album_titles = []
            for album_title, songs in albums_dict.items():
                b.album_titles += [album_title]
                if len(search_frase) == 0 or album_title.find(search_frase) > -1:
                    a = Album()
                    a.band = b
                    a.title = album_title
                    a.songs = []
                    for idx, song_title in songs:
                        a.songs += [song_title]
                    album_list += [a]
        return album_list
  

