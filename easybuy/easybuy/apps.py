# easybuy/apps.py

from django.apps import AppConfig

class EasyBuyConfig(AppConfig):
    name = 'easybuy'

    def ready(self):
        import easybuy.signals  # Import signals here
