from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.
class Notification1(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(max_length=20)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    def __str__(self):
        return f'{self.actor} {self.verb} {self.content_object}'

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    notifications = GenericRelation(Notification1)
    def __str__(self):
        return f'Task:{self.name}'

class Supervisor(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE, related_name="supervisor")
    task = models.ManyToManyField(Task,related_name='tasks')
    notifications = GenericRelation(Notification1)
    def __str__(self):
        return f'{self.user.username}'
class Employee(models.Model):
    employee_number = models.IntegerField()
    employee_name = models.CharField(max_length=30)
    employee_salary =  models.FloatField()
    def __str__(self):
        return self.employee_name

