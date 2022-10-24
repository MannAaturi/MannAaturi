from django.contrib import admin
from .models import Message, Video, Pdf

# Register your models here.

admin.site.register((Message, Video, Pdf))