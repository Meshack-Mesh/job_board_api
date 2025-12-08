from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
