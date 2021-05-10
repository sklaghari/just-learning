from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import \
    (Task,Supervisor,Notification1,Employee)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name']
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ['user']



admin.site.register(Task,TaskAdmin)
admin.site.register(Notification1)
admin.site.register(Employee)
admin.site.register(Supervisor,SupervisorAdmin)












