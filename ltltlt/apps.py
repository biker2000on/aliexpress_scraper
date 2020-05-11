from django.apps import AppConfig


class LtltltConfig(AppConfig):
    name = 'ltltlt'
    def ready(self):
        from price_updater import updater
        updater.start()
