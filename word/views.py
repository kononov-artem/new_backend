import json

from django.contrib.auth.models import User
from django.http import HttpResponseServerError, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView, FormView
from word.forms import LanguagesForm, WordsForm, DictionariesForm
from word.models import Languages, Words, Dictionaries, Translate


class LanguagesView(FormView):
    template_name = 'word/languages.html'
    form_class = LanguagesForm
    model = Languages

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return reverse('word_languages')


class WordsView(FormView):
    template_name = 'word/words.html'
    form_class = WordsForm
    model = Words

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return reverse('word_languages')


class DictionariesView(FormView):
    template_name = 'word/dictionaries.html'
    form_class = DictionariesForm
    model = Dictionaries

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return reverse('word_dictionaries')


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('UTF-8'))
        data = json_data[0]
        print(data)
        dictionary = data['dictionary']
        language = dictionary['language']
        language_to = dictionary['language_to']
        words = dictionary['words']
        name = dictionary['name']
        create_new = True if dictionary['create_new'] == 'true' else False
        lang = _add_language(language)
        lang_to = _add_language(language_to)

        if create_new:
            d = Dictionaries()
            d.name = name
            d.language = lang
            d.language_to = lang_to
            d.save()
        else:
            d = Dictionaries.objects.get(name=name)
        get_language = lang_to
        get_language_to = lang
        for item in words:
            original = item['original']
            translate = item['translate']
            if not Words.objects.filter(word=original).exists():
                word1 = _save_word(get_language, original)
            else:
                word1 = Words.objects.get(word=original)
            if not Words.objects.filter(word=translate).exists():
                word2 = _save_word(get_language_to, translate)
            else:
                word2 = Words.objects.get(word=translate)

            translate = Translate()
            translate.word = word1
            translate.translate = word2
            translate.language = get_language
            translate.language_to = get_language_to
            translate.save()
            d.translate.add(translate)
            print(original, translate)
        user = User.objects.get(pk=1)
        d.user.add(user)
    return render(request, 'word/dictionaries.html', {})


def _add_language(language):
    lang = Languages.objects.filter(language=language)
    if not lang.exists():
        lang = Languages()
        lang.language = language
        lang.save()
    else:
        lang = lang[0]
    return lang


def _save_word(language, word):
    obj = Words()
    obj.word = word
    obj.language = language
    obj.save()
    return obj


def get_data(request):
    dictionary = request.GET['dictionary']
    d = Dictionaries.objects.get(name=dictionary)
    name = d.name
    users = d.user.all()
    language = d.language.language
    language_to = d.language_to.language
    translates = d.translate.all()
    lst = []
    for translate in translates:
        print(translate.word.word, translate.translate.word)
        dct = {
            'original': translate.word.word,
            'translate': translate.translate.word
        }
        lst.append(dct)
    print(name, language, language_to)
    print(request.user)
    return JsonResponse({
        'user': str(users[0]),
        'name': name,
        'language': language,
        'language_to': language_to,
        'words': lst
    })


def get_your_dct(request):
    user = User.objects.get(pk=1)
    dicts = Dictionaries.objects.filter(user__pk=user.pk)
    dicts = [dct.name for dct in dicts]

    response = JsonResponse({
        'dicts': dicts,
    })
    return response


def word_traine_get_word(request):
    words = Translate.objects.all()
    data = []
    for word in words:
        if word.word and word.translate:
            data.append({
                'original': word.word.word,
                'translate': word.translate.word,
            })
    # print(data)
    response = JsonResponse({
        'words': data
    })
    return response


@csrf_exempt
def word_traine_check_word(request):
    answer = False
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('UTF-8'))
        data = json_data[0]
        answer = Translate.objects.filter(word__word=data['word'], translate__word=data['translate']).first()
        if answer:
            answer = True
        else:
            answer = False

    response = JsonResponse({
        'answer': answer,
    })
    return response

