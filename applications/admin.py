from django.contrib import admin
from .models import Application
from django.utils.html import format_html

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'applicant_link', 'job_link', 'applied_at', 'status_colored']
    ordering = ['-applied_at']
    list_filter = ['status', 'job']
    search_fields = ['applicant__username', 'job__title']

    def applicant_link(self, obj):
        return f"{obj.applicant.username}"
    applicant_link.short_description = 'Applicant'
    applicant_link.admin_order_field = 'applicant'

    def job_link(self, obj):
        return f"{obj.job.title}"
    job_link.short_description = 'Job'
    job_link.admin_order_field = 'job'

    def status_colored(self, obj):
        colors = {
            'pending': 'orange',
            'reviewed': 'blue',
            'accepted': 'green',
            'rejected': 'red',
        }
        color = colors.get(obj.status, 'black')
        return format_html('<span style="color: {};">{}</span>', color, obj.get_status_display())
    status_colored.short_description = 'Status'
