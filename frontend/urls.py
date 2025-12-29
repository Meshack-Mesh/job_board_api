from django.urls import path
from .views import dashboard, jobs_ui, companies_ui, applications_ui

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('jobs-ui/', jobs_ui, name='jobs_ui'),
    path('companies-ui/', companies_ui, name='companies_ui'),
    path('applications-ui/', applications_ui, name='applications_ui'),
]
