from rest_framework import serializers
from .models import Tasks

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','task_name','task_description','date_of_task']