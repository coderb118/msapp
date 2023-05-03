from django.contrib import admin
from .models import *

class MsLoginRDBMS(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'email', 'password1', 'password2', 'date', 'update_date')


class MsBlackListRDBMS(admin.ModelAdmin):
    list_display = ('id', 'email', 'date', 'update_date')






admin.site.register(MsLogin, MsLoginRDBMS)
admin.site.register(MsBlacklist)
admin.site.register(Msworks)
