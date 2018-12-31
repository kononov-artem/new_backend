import logging

from django.http import JsonResponse

from word.models import Dictionaries


logger = logging.getLogger(__name__)


def get_list_of_dicts_by_user(request):
    dicts = Dictionaries.objects.filter(user=request.user)

    logger.info(f'response by {request}, dicts length {len(dicts)}')

    data = []
    for dictionary in dicts:
        data.append({
            'name': dictionary.name,
            'date': str(dictionary.date),
            'language': str(dictionary.language),
            'language_to': str(dictionary.language_to),
        })

    return JsonResponse(data, safe=False)
