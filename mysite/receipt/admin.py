from django.contrib import admin

# Register your models here.

from .models import Receipt,Store

admin.site.register(Receipt)
admin.site.register(Store)