import time

from django.db import models
from django_countries.fields import CountryField


class AbstractTracked(models.Model):
    class Meta:
        abstract = True

    ctime = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')
    mtime = models.DateTimeField(auto_now=True, verbose_name='Update time')


def image_upload_to(instance, filename: str) -> str:
        return f'images/{int(time.time())}{filename}'


class Brewery(AbstractTracked):
    name = models.CharField(max_length=255, null=False)
    country = CountryField(null=True)
    description = models.TextField(max_length=2000)
    logo = models.ImageField(upload_to=image_upload_to, null=True)
    link = models.URLField(null=True)

    def __str__(self):
        return self.name


class Style(AbstractTracked):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Beer(AbstractTracked):
    name = models.CharField(null=False, max_length=255)
    brewery = models.ForeignKey(Brewery, null=True, on_delete=models.DO_NOTHING)
    style = models.ManyToManyField(Style, null=True)
    description = models.TextField(max_length=2000, null=True)
    image = models.ImageField(null=True, upload_to=image_upload_to)
    link = models.URLField(null=True)
    abv = models.DecimalField(decimal_places=2, max_digits=4, null=True)

    def __str__(self):
        return self.name


class Event(AbstractTracked):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    starttime = models.DateTimeField(null=False)
    endtime = models.DateTimeField(null=False)
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Session(AbstractTracked):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    starttime = models.DateTimeField(null=False)
    endtime = models.DateTimeField(null=True)
    beers = models.ManyToManyField(Beer)
    room = models.URLField(null=True, blank=True)
    stream = models.URLField(null=True, blank=True)
    agenda = models.TextField(max_length=2000)
    logo = models.ImageField(null=True) 

    def __str__(self):
        return self.name

