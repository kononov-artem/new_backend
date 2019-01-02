from django.contrib.auth.models import User, Group
from rest_framework import serializers

from word.models import Languages, Words, Translate, Dictionaries


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class LanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = ('id', 'language', 'is_approve', 'is_in_translate')


class WordsSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        read_only=True,
        slug_field='language'
    )

    class Meta:
        model = Words
        fields = ('word', 'language', 'is_approve', 'is_in_translate')


class TranslateSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        read_only=True,
        slug_field='language'
    )
    language_to = serializers.SlugRelatedField(
        read_only=True,
        slug_field='language'
    )
    word = serializers.SlugRelatedField(
        read_only=True,
        slug_field='word'
    )
    translate = serializers.SlugRelatedField(
        read_only=True,
        slug_field='word'
    )

    class Meta:
        model = Translate
        fields = ('language', 'language_to', 'word', 'translate')


class DictionariesSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        read_only=True,
        slug_field='language'
    )
    language_to = serializers.SlugRelatedField(
        read_only=True,
        slug_field='language'
    )
    user = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user_detail'
    )
    translate = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='translate_detail'
    )

    class Meta:
        model = Dictionaries
        fields = ('name', 'is_approve', 'date', 'language', 'language_to', 'translate', 'user')


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class TranslateDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    word = serializers.CharField(max_length=100)
    translate = serializers.CharField(max_length=100)


class LanguageDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    language = serializers.CharField(max_length=100)
    is_approve = serializers.BooleanField()
    is_in_translate = serializers.BooleanField()


class LanguagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('language',)
