import pandas as pd
from django.core.management import BaseCommand

from word.models import Languages, Words, Translate


class Command(BaseCommand):

    def handle(self, *args, **options):
        df = pd.read_csv('/Users/artem/Documents/my_project/cursa/MyProjects/words.csv')
        print(df)
        en = Languages.objects.get(language='English')
        ru = Languages.objects.get(language='Russian')
        for i, row in df.iterrows():
            word_en = Words.objects.create(word=row['word'], language=en).save()
            word_ru = Words.objects.create(word=row['translate'], language=ru).save()
            Translate.objects.create(language=en, language_to=ru, word=word_en, translate=word_ru).save()
