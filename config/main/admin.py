from django.contrib import admin
from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'special', 'address', 'phone_number')


admin.site.register(Restaurant,RestaurantAdmin)
