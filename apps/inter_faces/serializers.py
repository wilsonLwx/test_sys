# __author__ = 'wilsonLwx'
# __date__ = '2018/10/16'
from rest_framework import serializers

from .models import InterfaceList


class InterfaceListSerializer(serializers.Serializer):
    class Mete:
        model = InterfaceList
        fields = '__all__'
