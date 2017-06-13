from django.db import models
import helper
import uuid
# Create your models here.


class Comix(object):
    """docstring for Comix"""
    plot = models.TextField()
    title = models.CharField(max_length=300)
    id_comix = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    views = models.BigIntegerField()
    cover = models.CharField(max_length=50)

class Chapter(object):
    """docstring for Chapter"""
    