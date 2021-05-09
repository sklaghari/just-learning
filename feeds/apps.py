from django.apps import AppConfig


class FeedsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feeds'
    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        registry.register(User)
        registry.register(self.get_model('Task'), self.get_model('Supervisor'))