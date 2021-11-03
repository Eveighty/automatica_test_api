from django.contrib import admin
from django.db import models
from .models import Employee, RetailPoint, Visit


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    model = Employee

    list_display = ['name', 'phone']
    search_fields = ['name', 'phone']

@admin.register(RetailPoint)
class AdminRetailPoint(admin.ModelAdmin):
    model = RetailPoint

    list_display = ['id', 'title', 'employee']
    list_display_links = ['id', 'title', 'employee']

@admin.register(Visit)
class AdminVisit(admin.ModelAdmin):
    model = Visit

    save_as_continue = False
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ['retail_point', 'visit_date', 'coordinates']

    list_display = ['visit_date', 'retail_point', 'coordinates']
    list_display_links = ['visit_date', 'retail_point', 'coordinates']


admin.site.site_title = "Automatica admin"
admin.site.site_header = "Automatica"