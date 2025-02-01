from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name', 'description', 'created_at', 'updated_at', 'status')
    search_fields = ('name',)

admin.site.register(Department, DepartmentAdmin)
