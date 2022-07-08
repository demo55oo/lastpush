from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Message(models.Model):
        body = models.TextField()
        ip = models.TextField(null=True)
        cname = models.TextField(null=True)
        txt = models.TextField(null=True)
        updated = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-updated', '-created']
        def __str__(self):
            return self.body[0:50]
