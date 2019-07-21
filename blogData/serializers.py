from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MisPerros

class PerrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MisPerros
        fields = ['Nombre','Detalles','Foto','Disponibilidad']
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']