from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Muestra


class MuestraSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Muestra
        fields = ('codigo','owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    muestras = serializers.HyperlinkedRelatedField(many=True, view_name='muestra-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'muestras')