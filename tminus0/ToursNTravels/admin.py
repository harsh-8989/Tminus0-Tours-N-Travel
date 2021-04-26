from django.contrib import admin

# Register your models here.
from .models import user, location, review, history, flight, train, hotel, history, payment, attraction

# Register your models here.
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'region']
