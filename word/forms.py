from django import forms

from word.models import Languages, Words, Dictionaries


class LanguagesForm(forms.ModelForm):

    class Meta:
        model = Languages
        fields = [
            'language'
        ]


class WordsForm(forms.ModelForm):

    class Meta:
        model = Words
        fields = [
            'word'
        ]


class DictionariesForm(forms.ModelForm):

    class Meta:
        model = Dictionaries
        fields = [
            'name'
        ]
