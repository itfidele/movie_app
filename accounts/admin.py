from django.contrib import admin

from accounts.models import Category, Movies

# Register your models here.
admin.site.register(Category)
admin.site.register(Movies)