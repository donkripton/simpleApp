from django.contrib import admin

from dataStorage.models import EmployeeInfo
# Register your models here.

class EmployeeInfoAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'email')

admin.site.register(EmployeeInfo, EmployeeInfoAdmin)