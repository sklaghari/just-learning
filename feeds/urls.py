import notifications
from django.urls import path,re_path, include
from django.conf.urls.static import static
from .views import feeds,create_tasks,follow_view, unfollow_view, notifications,employee_view
from django.conf import settings
app_name='feeds'
urlpatterns = [
    path('', feeds, name='feeds'),
    path('create', create_tasks, name='create_task'),
    path('follow/<int:id>', follow_view, name='follow_view'),
    path('unfollow/<int:id>', unfollow_view, name='unfollow_view'),
    path('notification',notifications, name = 'notification'),
    path('employeeapi', employee_view.as_view(), name='employeeapi'),
    re_path('^activity/', include('actstream.urls')),
    re_path('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
