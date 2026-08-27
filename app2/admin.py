from django.contrib import admin
from .models import BMIRecord

@admin.register(BMIRecord)
class BMIRecordAdmin(admin.ModelAdmin):
    list_display = ['name','weight','height','bmi','category','created_at']
    list_filter = ['category']
    search_fields = ['name']

# Register your models here.
