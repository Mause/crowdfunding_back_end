from rest_framework import serializers
from .models import Project, Pledge
from django.apps import apps

# Pledge Serializer
class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields ='__all__'
        # read_only_fields = ['id', 'supporter']  # Fields that should not be writable by the user

# Pledge Detail Serializer (optional, for more specific details if needed)
class PledgeDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    project_name = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'supporter', 'project', 'project_name']
        read_only_fields = ['id', 'supporter', 'project', 'project_name']

# Project Serializer for listing all projects
class ProjectSerializer(serializers.ModelSerializer):
    # Include the owner's username if needed in the serialized output
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal', 'image', 'is_open', 'date_created', 'owner']
        read_only_fields = ['id', 'date_created', 'owner']  # Fields that should not be writable by the user

# Project Detail Serializer for individual project view
class ProjectDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Nested pledges: Fetch all related pledges for a project
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'goal', 'image', 'is_open', 
            'date_created', 'owner', 'pledges'
        ]
        read_only_fields = ['id', 'date_created', 'owner', 'pledges']  # Fields that should not be writable by the user
