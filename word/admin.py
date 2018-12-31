from django.contrib import admin

from word.models import Languages, Words, Translate, Dictionaries

admin.site.register(Dictionaries)
admin.site.register(Translate)
admin.site.register(Words)
admin.site.register(Languages)
