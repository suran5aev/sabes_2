from rest_framework import serializers
from apps.todo.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','descriptions','completed','created']