from django.db import models
from companies.models import Company
from datetime import datetime 

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("FT", "Full-time"),
        ("PT", "Part-time"),
        ("CT", "Contract"),
        ("IN", "Internship"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    job_type = models.CharField(
        max_length=2,
        choices=JOB_TYPE_CHOICES, default= 'Part-time'
    ) 
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
