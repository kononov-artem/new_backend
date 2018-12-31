import datetime

from django.contrib.auth.models import User
from django.db import models


class Languages(models.Model):
    language = models.CharField(max_length=200)
    is_approve = models.BooleanField(default=False)
    is_in_translate = models.BooleanField(default=False)

    def __str__(self):
        return self.language


class Words(models.Model):
    word = models.CharField(max_length=200)
    is_approve = models.BooleanField(default=False)
    is_in_translate = models.BooleanField(default=False)
    language = models.ForeignKey(Languages, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.word


class Translate(models.Model):
    language = models.ForeignKey(Languages, models.SET_NULL, related_name='translate_from', blank=True, null=True)
    language_to = models.ForeignKey(Languages, models.SET_NULL, related_name='translate_to', blank=True, null=True)
    word = models.ForeignKey(Words, models.SET_NULL, related_name='word_from', blank=True, null=True)
    translate = models.ForeignKey(Words, models.SET_NULL, related_name='word_to', blank=True, null=True)

    def __str__(self):
        return str(self.language) + ' -> ' + str(self.language_to) + ' word: ' \
               + str(self.word) + ' -> ' + str(self.translate)


class Dictionaries(models.Model):
    name = models.CharField(max_length=200)
    is_approve = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.datetime.now())
    language = models.ForeignKey(Languages, models.SET_NULL, related_name='language_from', blank=True, null=True)
    language_to = models.ForeignKey(Languages, models.SET_NULL, related_name='language_to', blank=True, null=True)
    translate = models.ManyToManyField(Translate)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


def clear():
    Translate.objects.all().delete()
    Dictionaries.objects.all().delete()
    Words.objects.all().delete()
    Languages.objects.all().delete()
