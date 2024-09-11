from rest_framework import serializers
from .models import Task, Label

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name', 'owner']

class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'owner', 'labels']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and not request.user.is_staff:
            self.fields['title'].read_only = True
            self.fields['description'].read_only = True
            self.fields['owner'].read_only = True

    def update(self, instance, validated_data):
        validated_data.pop('owner', None)
        return super().update(instance, validated_data)