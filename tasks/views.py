from rest_framework.viewsets import ModelViewSet
from .models import Tasks
from .serializers import TaskSerializers

class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers

