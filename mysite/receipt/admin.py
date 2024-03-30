from django.contrib import admin

# Register your models here.

from .models import Receipt,Store,Item

admin.site.register(Receipt)
admin.site.register(Store)
admin.site.register(Item)