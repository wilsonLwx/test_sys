from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import InterfaceList
from .serializers import InterfaceListSerializer


# Create your views here.

class InterfaceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list all of Interfaces
    """
    queryset = InterfaceList.objects.all()
    serializer_class = InterfaceListSerializer
