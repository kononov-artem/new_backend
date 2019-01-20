import json

from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from api.serializers import UserListSerializer, GroupListSerializer, LanguagesSerializer, WordsSerializer, \
    TranslateSerializer, \
    DictionariesSerializer, UserDetailSerializer, TranslateDetailSerializer, LanguageDetailSerializer, \
    LanguagePostSerializer, WordPostSerializer, DictionaryDetailSerializer
from word.models import Languages, Words, Translate, Dictionaries


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserListSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Group.objects.all()
    serializer_class = GroupListSerializer


class LanguagesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        languages = Languages.objects.all()
        serializer = LanguagesSerializer(languages, many=True)
        return Response(serializer.data)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class WordsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    pagination_class = LargeResultsSetPagination

class TranslateView(APIView):

    def get(self, request):
        start_index = int(request.GET.get('startIndex', 0))
        stop_index = int(request.GET.get('stopIndex', Translate.objects.all().count()))

        translate = Translate.objects.all()[start_index:stop_index + 1]
        serializer = TranslateSerializer(translate, many=True)
        return Response(serializer.data)


class DictionariesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # .filter(Q(income__gte=5000) | Q(income__isnull=True))
        dictionaries = Dictionaries.objects.filter(user=request.user)
        serializer = DictionariesSerializer(dictionaries, many=True, context={'request': request})
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class TranslateDetailDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Translate.objects.get(pk=pk)
        except Translate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        translate = self.get_object(pk)
        serializer = TranslateDetailSerializer(translate)
        return Response(serializer.data)


class LanguageDetailDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Languages.objects.get(pk=pk)
        except Translate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageDetailSerializer(language)
        return Response(serializer.data)


class DictionaryDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Dictionaries.objects.get(pk=pk, user=user)
        except Translate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dictionary = self.get_object(pk, request.user)
        serializer = DictionaryDetailSerializer(dictionary)
        return Response(serializer.data)


class LanguageAdd(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        language = LanguagePostSerializer(data=request.data)
        if language.is_valid():
            language.save()
            return Response({'status': 'ok'})
        return Response({'status': 'error'})


class WordAdd(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_language_id(self, language):
        try:
            language_obj = Languages.objects.get(language=language)
        except Translate.DoesNotExist:
            raise Http404
        return language_obj.id

    def post(self, request):
        request.data['language'] = self.get_language_id(request.data['language'])
        word = WordPostSerializer(data=request.data)
        if word.is_valid():
            word.save()
            return Response({'status': 'ok'})
        return Response({'status': 'error'})


class DictionariesUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_dict_obj(self, id):
        try:
            dictionary_obj = Dictionaries.objects.get(pk=id)
        except Translate.DoesNotExist:
            raise Http404
        return dictionary_obj

    def post(self, request):
        dictionaries = request.data['data']
        for dictionary in dictionaries:
            dictionary_obj = self.get_dict_obj(dictionary['id'])
            if 'name' in dictionary:
                dictionary_obj.name = dictionary['name']
            if 'is_active' in dictionary:
                dictionary_obj.is_active = dictionary['is_active']
            # TODO: add translate and delete
            dictionary_obj.save()
        return Response({'status': 'ok'})


class CheckPermission(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        data = {}
        if user.is_superuser:
            data['permission'] = 'superuser'
        return Response(data)


class GetTokenByUser(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        return user

    def post(self, request, format=None):
        username = request.data['data']['username']
        user = self.get_user(username)
        data = {'token': user.auth_token.key}
        return Response(data)


class SearchWord(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_words(self, word):
        try:
            words = Words.objects.filter(word__startswith=word).extra(select={'length': 'Length(word)'}).order_by(
                'length'
            )[:10]
        except User.DoesNotExist:
            raise Http404
        return words

    def post(self, request, format=None):
        word = request.data['word']
        words = self.get_words(word)
        serializer = WordsSerializer(words, many=True)
        return Response(serializer.data)


class SearchTranslate(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_translate(self, word):
        try:
            translate = Translate.objects.filter(word__word=word).first()
        except User.DoesNotExist:
            raise Http404
        return translate

    def post(self, request, format=None):
        word = request.data['word']
        tanslate = self.get_translate(word)
        if tanslate:
            word = tanslate.translate
        else:
            word = None
        serializer = WordsSerializer(word)
        return Response(serializer.data)
