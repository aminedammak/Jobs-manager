from django.shortcuts import render
from .serializers import LanguageSerializer, ParadigmSerializer, DeveloperSerializer
from .models import Language, Paradigm, Developer
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class DeveloperView(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer






