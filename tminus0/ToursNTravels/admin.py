from django.contrib import admin

# Register your models here.
from .models import User, Location, Review, History, Flight, Train, Hotel, History, Payment, Attraction

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'region']
