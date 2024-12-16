from rest_framework import serializers
from .models import Project, Pledge  # Import both Project and Pledge models

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')  # Read-only field for the supporter ID
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Validates project by ID
    comment = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )  # Allow blank or null comments

    class Meta:
        model = Pledge
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project  # Ensure the Project model is used
        fields = '__all__'  # Serialize all fields in the model


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)  # Nested PledgeSerializer to show pledges

    class Meta:
        model = Project  # Ensure the Project model is used
        fields = '__all__'  # Serialize all fields in the model

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class PledgeDetailSerializer(PledgeSerializer):
    # Custom update method for the PledgeDetailSerializer
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.save()
        return instance

