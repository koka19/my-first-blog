# 10_W4 modellierten Posts hinzuzufügen, zu ändern oder zu löschen.

from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Register your models here.
