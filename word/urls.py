from django.conf.urls import url

from word.views.get_dictionary_by_name import get_dictionary_by_name
from word.views.list_of_dicts_by_user import get_list_of_dicts_by_user


urlpatterns = [
    # url(r'^dictionaries/json/', save_data, name='word_dictionaries_json'),
    url(r'^dictionaries/get/', get_dictionary_by_name, name='word_dictionaries_get'),
    url(r'^dictionaries/list/', get_list_of_dicts_by_user, name='word_dictionaries_list_of_dicts'),
    # url(r'^dictionaries/traine/getWord', word_traine_get_word, name='word_traine_get_word'),
    # url(r'^dictionaries/traine/check', word_traine_check_word, name='word_traine_check'),
]
