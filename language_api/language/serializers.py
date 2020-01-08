from rest_framework import serializers
from .models import Language, Paradigm, Developer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "url", "name", "paradigm")


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ("id", "url", "name")


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ("id", "url", "name", "programmingLanguages")