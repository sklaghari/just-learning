from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Task,Supervisor,Notification1
@receiver(post_save,sender = Supervisor)
def task_assigned_signal(sender,instance,created,**kwargs):
    if created:
        Notification1(actor = instance.user, verb="has been assigned",content_object=Task)

