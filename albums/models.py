from django.db import models
from django.utils import timezone
# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
