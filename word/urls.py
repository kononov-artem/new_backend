from django.conf.urls import url

from word import views
from word.views import save_data, get_data, get_your_dct, word_traine_get_word, word_traine_check_word

urlpatterns = [
    url(r'^languages/add/', views.LanguagesView.as_view(), name='word_languages'),
    url(r'^words/add/', views.WordsView.as_view(), name='word_words'),
    url(r'^dictionaries/add/', views.DictionariesView.as_view(), name='word_dictionaries'),
    url(r'^dictionaries/json/', save_data, name='word_dictionaries_json'),
    url(r'^dictionaries/get/', get_data, name='word_dictionaries_get'),
    url(r'^dictionaries/your_dict/', get_your_dct, name='word_dictionaries_get_your'),
    url(r'^dictionaries/traine/getWord', word_traine_get_word, name='word_traine_get_word'),
    url(r'^dictionaries/traine/check', word_traine_check_word, name='word_traine_check'),
]





