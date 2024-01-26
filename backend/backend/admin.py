from django.contrib import admin
from .models import *
from django.db import models
for mod in models.Model.__subclasses__():
    try:
        admin.site.register(mod)
        pass
    except:
        pass
