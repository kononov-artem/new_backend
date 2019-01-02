from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserListSerializer, GroupListSerializer, LanguagesSerializer, WordsSerializer, \
    TranslateSerializer, \
    DictionariesSerializer, UserDetailSerializer, TranslateDetailSerializer, LanguageDetailSerializer, \
    LanguagePostSerializer, WordPostSerializer
from word.models import Languages, Words, Translate, Dictionaries


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserListSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer


class LanguagesView(APIView):

    def get(self, request):
        languages = Languages.objects.all()
        serializer = LanguagesSerializer(languages, many=True)
        return Response(serializer.data)


class WordsView(APIView):

    def get(self, request):
        words = Words.objects.all()
        serializer = WordsSerializer(words, many=True)
        return Response(serializer.data)


class TranslateView(APIView):

    def get(self, request):
        translate = Translate.objects.all()
        serializer = TranslateSerializer(translate, many=True)
        return Response(serializer.data)


class DictionariesView(APIView):

    def get(self, request):
        dictionaries = Dictionaries.objects.all()
        serializer = DictionariesSerializer(dictionaries, many=True, context={'request': request})
        return Response(serializer.data)


class UserDetail(APIView):

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

    def get_object(self, pk):
        try:
            return Languages.objects.get(pk=pk)
        except Translate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageDetailSerializer(language)
        return Response(serializer.data)


class LanguageAdd(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        language = LanguagePostSerializer(data=request.data)
        if language.is_valid():
            language.save()
            return Response({'status': 'ok'})
        return Response({'status': 'error'})


class WordAdd(APIView):

    permission_classes = [permissions.AllowAny]

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
