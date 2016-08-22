from django.contrib import admin
from accounts.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',  'regNo', 'phoneNumber', 'national_id', 'school', 'department']

    class Meta:
        model = Profile
admin.site.register(Profile, ProfileAdmin)


class IdApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'regNo', 'full_name', 'paid', 'date_applied']

    class Meta:
        model = IdApplication
admin.site.register(IdApplication, IdApplicationAdmin)
