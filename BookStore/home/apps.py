from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    # def ready():     // used for register signals because it is invoked when app init
    #     pass