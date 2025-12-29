from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from jobs.models import Job
from companies.models import Company
from applications.models import Application


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def jobs_ui(request):
    jobs = Job.objects.select_related('company').all()
    return render(request, 'jobs.html', {'jobs': jobs})


@login_required
def companies_ui(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})


@login_required
def applications_ui(request):
    applications = Application.objects.select_related('job', 'user').all()
    return render(request, 'applications.html', {'applications': applications})
