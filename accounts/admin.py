from django.contrib import admin
from accounts.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',  'regNo', 'phoneNumber', 'national_id', 'school', 'department', 'course']

    class Meta:
        model = Profile
admin.site.register(Profile, ProfileAdmin)


class IdApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'application_type', 'paid', 'date_applied']

    class Meta:
        model = IdApplication
admin.site.register(IdApplication, IdApplicationAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name']

    class Meta:
        model = School
admin.site.register(School, SchoolAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']

    class Meta:
        model = Department
admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['department', 'course_name']

    class Meta:
        model = Course
admin.site.register(Course, CourseAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['phoneNumber', 'message']

    class Meta:
        model = ContactMessage
admin.site.register(ContactMessage, ContactMessageAdmin)

