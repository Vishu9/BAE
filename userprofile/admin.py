from django.contrib import admin

# Register your models here.
#admin.site.register(Profile)
from .models import Profile, Imagepost

admin.site.register(Profile)
admin.site.register(Imagepost)