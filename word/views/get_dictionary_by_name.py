import logging

from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from word.models import Dictionaries


logger = logging.getLogger(__name__)


def get_dictionary_by_name(request):
    dictionary = request.GET.get('dictionary')
    if not dictionary:
        raise Http404

    user = request.user
    custom_dict = get_object_or_404(Dictionaries, name=dictionary, user=user)
    translates = custom_dict.translate.all()

    words = []
    for translate in translates:
        dct = {
            'original': translate.word.word,
            'translate': translate.translate.word
        }
        words.append(dct)

    logger.info(
        f'Return dictionary: '
        f'user: {user}, '
        f'dict name: {custom_dict.name}'
    )

    return JsonResponse({
        'user': str(user),
        'name': custom_dict.name,
        'language': custom_dict.language.language,
        'language_to': custom_dict.language_to.language,
        'words': words
    })
