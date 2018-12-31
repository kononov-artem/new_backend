from django.conf.urls import url

from word.views import (
    save_data,
    git_ditionary_by_name,
    get_your_dct,
    word_traine_get_word,
    word_traine_check_word,
)

urlpatterns = [
    url(r'^dictionaries/json/', save_data, name='word_dictionaries_json'),
    url(r'^dictionaries/get/', git_ditionary_by_name, name='word_dictionaries_get'),
    url(r'^dictionaries/your_dict/', get_your_dct, name='word_dictionaries_get_your'),
    url(r'^dictionaries/traine/getWord', word_traine_get_word, name='word_traine_get_word'),
    url(r'^dictionaries/traine/check', word_traine_check_word, name='word_traine_check'),
]





