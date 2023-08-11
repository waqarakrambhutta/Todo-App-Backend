from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name= models.CharField(max_length=100)
    task_description = models.CharField(max_length=255)
    date_of_task = models.DateTimeField(auto_now_add=True)  


    def __str__(self) -> str:
        return self.task_name