from django.contrib import admin

# Register your models here.
from .models import AuthUser, Superheroes

admin.site.register(AuthUser)
admin.site.register(Superheroes)