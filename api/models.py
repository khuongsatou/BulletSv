from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.

class Note(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, default=None, blank=True)
    description = models.CharField(max_length=100, null=True, default=None, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Detail(models.Model):
    id_note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=100, null=True, default=None, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
