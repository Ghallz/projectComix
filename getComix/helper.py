import requests
import json
from django.conf import settings

class Request(object):
	"""docstring for Request"""
	def __init__(self):
		self.urlLibrary = settings.COMIX_URL['URL_LIBRARY']
		self.urlComix = settings.COMIX_URL['URL_COMIX']
		self.savePath = settings.COMIX_URL['SAVE_PATH']

	def getComix():
		