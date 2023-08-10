from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name= models.CharField(max_length=100)
    task_descrition = models.CharField(max_length=255)
    date_of_task = models.DateTimeField(auto_now_add=True)  
