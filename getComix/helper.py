import requests
import json
from django.conf import settings
from pprint import pprint
from .models import Comix, Chapter
import re
import os


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
                comixJson = response.json()[0]
                comix = Comix()
                comix.plot = comixJson['sinopse']
                comix.title = comixJson['titulo']
                comix.id_comix = comixJson['id']
                comix.year = comixJson['ano']
                comix.adult = comixJson['maioridade']
                comix.views = comixJson['views']
                comix.type = comixJson['tipo']
                comix.chapters = len(comixJson['capitulos'])
                # comix.save()

                for k in range(len(comixJson['capitulos'])):
                    chapterJson = comixJson['capitulos'][k]
                    comixChapter = Chapter()
                    comixChapter.mainPage = chapterJson['arquivo']
                    comixChapter.cover = chapterJson['url_capa']
                    # comixChapter.save()

                    mainChapterPage = requests.get(chapterJson['arquivo'])
                    raw = mainChapterPage.text
                    links = re.findall('(?<=data-lazy=")(.*?)(?=\")', raw)
                    return links[4]

                    for l in links:
                        match = re.search('.png', links[k])
                        if(match is not None):
                            """save file """
                            folder = os.path.abspath(os.path.join(
                                os.sep, 'home', 'galiza', 'comixDatabase', comixJson['titulo'], chapterJson['capitulo']))
                            fileName = l + ".jpg"
                            """
                            use os.path to check is folder exists
                            https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
                            """
                            # request.urlretrieve(links[k], filename)
                            return folder
            break
        # return teste
