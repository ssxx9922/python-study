from django.contrib import admin

# Register your models here.
from blog.models import article

admin.site.register(article)