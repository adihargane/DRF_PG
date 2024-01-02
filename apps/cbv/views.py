from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.cbv.models import VehicleModel
from apps.cbv.serializers import VehicleSerializer


# Create your views here.


class VehicleCRUD(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                vehicle = VehicleModel.objects.get(pk=pk)
                serializer = VehicleSerializer(vehicle)
                return Response({'Success': True, 'Data': serializer.data}, status=status.HTTP_200_OK)
            else:
                vehicle = VehicleModel.objects.all()
                # vehicle = VehicleModel.objects.filter(active=True).order_by('-uid')
                serializer = VehicleSerializer(vehicle, many=True)
                return Response({'Success': True, 'Data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data

            serializer = VehicleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Success': True, 'Message': 'Vehicle details added successfully', 'Data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'Success': False, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            if pk is None:
                return Response({'Success': False, 'Error': 'pk is required in params'}, status=status.HTTP_400_BAD_REQUEST)

            data = request.data

            try:
                vehicle = VehicleModel.objects.get(pk=pk)
            except Exception as e:
                return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

            serializer = VehicleSerializer(vehicle, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({'Success': True, 'Message': 'Vehicle details Updated Successfully', 'Data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'Success': False, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            if pk is None:
                return Response({'Success': False, 'Error': 'pk is required in params'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                vehicle = VehicleModel.objects.get(pk=pk)
            except Exception as e:
                return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

            vehicle.delete()
            return Response({'Success': True, 'Message': 'Vehicle details deleted successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)


class SoftVehicle(APIView):
    def get(self, request):
        try:
            vehicle = VehicleModel.objects.filter(active=True).order_by('-uid')
            serializer = VehicleSerializer(vehicle, many=True)
            return Response({'Success': True, 'Data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            data = request.data
            uid = data.get('uid', None)

            if uid is None:
                return Response({'Success': False, 'Error': 'uid is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                vehicle = VehicleModel.objects.get(pk=uid)
            except Exception as e:
                return Response({'Success': False, 'Error': e}, status=status.HTTP_404_NOT_FOUND)

            vehicle.active = False
            vehicle.save()
            return Response({'Success': True, 'Message': 'Vehicle details deleted successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Success': False, 'Error': e}, status=status.HTTP_400_BAD_REQUEST)
