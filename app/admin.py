from django.contrib import admin
from .models import Slider, Category,Club, Staff,News

# Регистрация моделей
admin.site.register(Slider)
admin.site.register(Category)
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience', 'is_active', 'order']
    list_filter = ['position', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')

