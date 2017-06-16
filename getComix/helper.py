import requests
import json
from django.conf import settings
from pprint import pprint
from .models import Comix, Chapter
import urllib
import re
import os

class Downloader(urllib.request.FancyURLopener):
    """docstring for FancyOpener"""
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

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
        for i in range(1, 2):
            # for i in range(1, totalPages):
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
                folder = os.path.abspath(os.path.join(
                    os.sep, 'home', 'fillipe', 'comixDatabase', comixJson['titulo']))
                if not os.path.exists(folder):
                    os.makedirs(folder)
                    os.chmod(folder, 0o777)
                for k in range(len(comixJson['capitulos'])):
                    chapterJson = comixJson['capitulos'][k]
                    comixChapter = Chapter()
                    comixChapter.mainPage = chapterJson['arquivo']
                    comixChapter.cover = chapterJson['url_capa']
                    # comixChapter.save()

                    mainChapterPage = requests.get(chapterJson['arquivo'])
                    raw = mainChapterPage.text
                    links = re.findall('(?<=data-lazy=")(.*?)(?=\")', raw)

                    count = 1
                    for l in links:
                        match = re.search('jpg', l)
                        if(match is not None):
                            """save file """
                            folder = os.path.abspath(os.path.join(
                                os.sep, 'home', 'fillipe', 'comixDatabase', comixJson['titulo'], chapterJson['capitulo']))
                            
                            if not os.path.exists(folder):
                                os.makedirs(folder)
                                os.chmod(folder, 0o777)

                            fileName = str(count) + ".jpg"
                            if not os.path.exists(folder +"/"+ fileName):
                                myOpener = Downloader()
                                myOpener.retrieve(l, folder +"/"+ fileName)
                            """
                            """
                        count += 1
            break
        # return teste


