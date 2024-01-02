from apps.cbv.models import VehicleModel
from rest_framework import serializers

#serializers

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'