from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.fbv.models import UserModel
from apps.fbv.serializers import UserSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def userList(request):
    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userDetailsByPk(request, pk):
    try:
        user = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def userMaster(request):
    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({'Success': True, 'Data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Success': True, 'Message': 'User Created Successfully', 'Data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Success': False, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        data = request.data
        uid = data.get('uid', None)

        if uid is None:
            return Response({'Success': False, 'Error': 'uid is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserModel.objects.get(pk=uid)
        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'Success': True, 'Message': 'User Updated Successfully', 'Data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Success': False, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data = request.data
        uid = data.get('uid', None)

        if uid is None:
            return Response({'Success': False, 'Error': 'uid is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserModel.objects.get(pk=uid)
        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'Success': True, 'Message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def softUserMaster(request):
    if request.method == 'GET':
        user = UserModel.objects.filter(active=1).order_by('-uid')      #-'keyword' => - descending order
        serializer = UserSerializer(user, many=True)
        return Response({'Success': True, 'Data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data = request.data
        uid = data.get('uid', None)

        if uid is None:
            return Response({'Success': False, 'Error': 'uid is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserModel.objects.get(pk=uid)
        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=data, partial=True)

        if serializer.is_valid():
            user.active = False
            user.save()
            return Response({'Success': True, 'Message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'Success': False, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
