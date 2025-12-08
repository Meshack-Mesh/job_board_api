from django.db import models
from companies.models import Company

class Job(models.Model):
    JOB_CATEGORIES = [
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=JOB_CATEGORIES)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.company.name}"
