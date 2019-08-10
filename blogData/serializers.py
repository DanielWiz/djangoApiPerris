from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MisPerros
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PerrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MisPerros
        fields = '__all__'
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

@api_view(['GET','POST'])
def lista_perritos(request):
    if request.method == "GET":
       perros = MisPerros.objects.all()
       serializer = PerrosSerializer(perros, many=True)
       return Response(serializer.data)
    else:  # Post
        serializer = PerrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  #Invalid data


@api_view(['GET','DELETE','PUT'])
def perros_detalle(request, id):
    try:
        perros = MisPerros.objects.get(id=id)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PerrosSerializer(perros)
        return Response(serializer.data)
    elif request.method == 'PUT':    # Update
        serializer = PerrosSerializer(perros, data=request.data)
        if serializer.is_valid():
           serializer.save()    # Update table in DB
           return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        perros.delete()
        return Response(status=204)