from django.http import HttpResponse
import requests
import json
from pprint import pprint
from django.conf import settings
import sys


def index(request):
    response = requests.get(settings.COMIX_URL['URL_LIBRARY']+'1')
    response = response.json()
    totalPages = response['num']
    return HttpResponse(totalPages)
    #     libraryPage = response['dados']
    #     for comix in libraryPage:
    #         print('STARTING COMIX ' + comix['titulo'] + '\n\n')
    #         chapter = requests.get(self.urlComix + comix['id'])
    #         pprint(chapter.json())
    #         break
