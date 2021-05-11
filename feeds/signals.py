from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .models import Task,Supervisor,Notification1
@receiver(post_save,sender = Supervisor)
def task_assigned_signal(sender,instance,created,**kwargs):
    if created:
        Notification1(actor = instance.user, verb="has been assigned",content_object=Task)
@receiver(post_save, sender = User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

