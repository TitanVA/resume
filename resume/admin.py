from django.contrib import admin

from resume.models import Resume, Job


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "get_name")
    list_display_links = ("id", "get_name")

    def get_name(self, obj):
        return f"{obj.employee.get_full_name()}: {obj.position}"
    get_name.short_description = 'Resume'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "get_employee")
    list_display_links = ("id", "name", "role")

    def get_employee(self, obj):
        return f"{obj.resumes.first()}"
    get_employee.short_description = 'Employee'
