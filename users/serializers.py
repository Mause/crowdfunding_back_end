from rest_framework import serializers
from .models import CustomUser
from projects.models import Pledge  # Import Pledge model

# CustomUser Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# Pledge Serializer (New)
class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge  # Reference to the Pledge model
        fields = ['amount', 'project', 'anonymous', 'comment']  # List the fields you want to serialize

    # Add any custom validation logic or methods if necessary

