from django.db import models
import uuid
# Create your models here.


class Comix(models.Model):
    """docstring for Comix"""
    plot = models.TextField()
    title = models.CharField(max_length=300)
    id_comix = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    views = models.BigIntegerField()
    cover = models.CharField(max_length=50)

    def __str__(self):
        return self.plot


class Chapter(models.Model):
    """docstring for Chapter"""
    comixId = models.ForeignKey(Comix, on_delete=models.CASCADE)
    mainPage = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
