from rest_framework import serializers
from apps.cbvusingquery.models import EmployeeModel, DocumentModel, EducationModel

#serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = '__all__'