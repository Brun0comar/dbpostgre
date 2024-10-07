from django.apps import AppConfig

class SuperheroesConfig(AppConfig):
    name = 'superheroes'

    def ready(self):
        import superheroes.signals 