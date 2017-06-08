from django.http import HttpResponse
from pprint import pprint
from .helper import Request


def index(request):
    teste = Request()
    teste2 = teste.getAllComix()
    return HttpResponse(teste2)
    #     libraryPage = response['dados']
    #     for comix in libraryPage:
    #         print('STARTING COMIX ' + comix['titulo'] + '\n\n')
    #         chapter = requests.get(self.urlComix + comix['id'])
    #         pprint(chapter.json())
    #         break
