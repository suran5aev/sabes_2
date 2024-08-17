from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class TaskAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.ListModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
