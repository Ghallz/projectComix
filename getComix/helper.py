import requests
import json
from django.conf import settings


class Request(object):
    """docstring for Request"""

    def __init__(self):
        self.urlLibrary = settings.COMIX_URL['URL_LIBRARY']
        self.urlComix = settings.COMIX_URL['URL_COMIX']
        self.savePath = settings.COMIX_URL['SAVE_PATH']

    def getTotalPages(self):
        response = requests.get(settings.COMIX_URL['URL_LIBRARY'] + '1')
        response = response.json()
        totalPages = response['num']
        return totalPages

    def getAllComix(self):
        totalPages = self.getTotalPages()
        for i in range(totalPages):
       		response = requests.get(settings.COMIX_URL['URL_LIBRARY'] + i)
       		response = response.json()
       		libraryPage = response['dados']
       		

        return teste
