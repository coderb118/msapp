from django.db import models
import uuid


class MsLogin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=True)
    ip_address = models.GenericIPAddressField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=500)
    password1 = models.CharField(max_length=200, null=True, blank=True)
    password2 = models.CharField(max_length=200, null=True, blank=True)

class MsBlacklist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=True)
    email = models.ForeignKey(MsLogin, on_delete=models.CASCADE)
    