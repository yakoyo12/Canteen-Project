from django.contrib import admin
from .models import Canteen

# Register your models here.
class CanteenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')





admin.site.register(Canteen, CanteenAdmin)
