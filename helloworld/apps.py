from django.apps import AppConfig
from viewflow import frontend

class HelloworldConfig(AppConfig):
    name = 'helloworld'

@frontend.register
class HelloWorldFlow(Flow):