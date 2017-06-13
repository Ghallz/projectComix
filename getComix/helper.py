  import requests
import json
from django.conf import settings
from pprint import pprint
from .models import Comix

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
        for i in range(1, totalPages):
            response = requests.get(settings.COMIX_URL['URL_LIBRARY'] + str(i))
            response = response.json()
            libraryPage = response['dados']
            for j in libraryPage:
                response = requests.get(
                    settings.COMIX_URL['URL_COMIX'] + str(j['id']))
                comixJson = response.json()
                comix = Comix()
                comix.plot = comixJson['sinopse']
                comix.title = comixJson['titulo']
                comix.id_comix = comixJson['id']
                comix.year = comixJson['ano']
                comix.adult = comixJson['maioridade']
                comix.views = comixJson['views']
                comix.type = comixJson['tipo']
                comix.chapters = comixJson['capitulos'].len()

                return comix
            break
        # return teste
