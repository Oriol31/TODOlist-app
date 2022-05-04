from django.contrib import admin
from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pub_date', 'date_to_complete', 'category', 'status')
    list_editable = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
