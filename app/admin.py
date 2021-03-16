from django.contrib import admin

# Register your models here.
from app.models import Company,User,Department

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UseAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass