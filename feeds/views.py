from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render
from notifications.models import Notification
from rest_framework.authtoken.models import Token
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

from .models import Notification1
from .models import Task,Supervisor,Employee
from actstream import action
from actstream.actions import follow,unfollow
from actstream.models import user_stream,actor_stream
from notifications.signals import notify
from .serializers import EmployeeSerilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet

all_users = User.objects.select_related('auth_token').all()
for user in all_users:
    Token.objects.get_or_create(user =user)
def feeds(request):
    userStream = user_stream(request.user, with_user_activity=True)
    context = {
        'stream': userStream,
        'notifications': Notification1.objects.all()
    }
    return render(request, 'feeds/action.html', context)
def create_tasks(request):
    assigned_task = Task.objects.create(name = 'UM', description = "Hello please UM")
    get_munir = User.objects.get(first_name = 'munir')
    supervisor_munir = Supervisor.objects.create(user = get_munir)
    supervisor_munir.task.add(assigned_task)
    assigned_task.notifications.create(actor= request.user, verb= 'assigned a task')
    Notification1.objects.create(content_object = assigned_task, actor = request.user,verb='abcd')
    return HttpResponse('see notifications')

def follow_view(request, id):
    instance = User.objects.get(id=id)
    follow(request.user,instance)
    return HttpResponse('followed')
def unfollow_view(request, id):
    instance = User.objects.get(id=id)
    unfollow(request.user,instance)
    return HttpResponse('Unfollowed')
def my_activity(request):
    pass
def notifications(request):
    qs = Notification.objects.all()
    context = {
        'notifications': qs.mark_all_as_active()
    }
    return render(request, 'feeds/notification.html', context)
class employeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerilizer
    permission_classes = [IsAuthenticated,]



