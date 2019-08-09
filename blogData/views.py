from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import PerrosSerializer
from .models import MisPerros
from rest_framework.views import APIView
from rest_framework.response import Response


class MisPerrosViewSet(viewsets.ModelViewSet):
    queryset = MisPerros.objects.filter(Disponibilidad='D')
    serializer_class = PerrosSerializer
    
    def get_paginated_response(self, data):
        return Response(data)
    
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer