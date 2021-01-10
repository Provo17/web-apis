from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profilesapi'

    def ready(self):
        import profilesapi.signals