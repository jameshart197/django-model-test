from django.contrib import admin
from .models import models
from django.apps import apps

# Register your models here.
models = apps.get_models()

for model in models:
    admin.site.register(model)
