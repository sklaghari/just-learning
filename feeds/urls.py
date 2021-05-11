import notifications
from django.urls import path,re_path, include
from django.conf.urls.static import static
from rest_framework import routers
from .views import feeds,create_tasks,follow_view, unfollow_view, notifications,employeeModelViewSet
from django.conf import settings
app_name='feeds'
router = routers.DefaultRouter()
router.register('api',employeeModelViewSet)
urlpatterns = [
    path('', feeds, name='feeds'),
    path('create', create_tasks, name='create_task'),
    path('follow/<int:id>', follow_view, name='follow_view'),
    path('unfollow/<int:id>', unfollow_view, name='unfollow_view'),
    path('notification',notifications, name = 'notification'),
    path('', include(router.urls)),
    re_path('^activity/', include('actstream.urls')),
    re_path('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
