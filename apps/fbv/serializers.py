from apps.fbv.models import UserModel
from rest_framework import serializers

#serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['uid', 'firstname', 'lastname', 'username', 'password', 'address', 'dob', 'active']