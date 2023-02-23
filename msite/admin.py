from django.contrib import admin
from .models import *

class MsLoginRDBMS(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'email', 'password1', 'password2')





admin.site.register(MsLogin, MsLoginRDBMS)
admin.site.register(MsBlacklist)
