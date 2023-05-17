from django.contrib import admin
from .models import Employee, Post, ViewLog, SearchLog, Category
# Register your models here.

admin.site.register([Employee, Post, ViewLog, SearchLog, Category])
