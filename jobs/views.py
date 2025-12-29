from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from .permissions import IsJobOwner
from companies.permissions import IsEmployer

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'location']

    def get_queryset(self):
        return Job.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsEmployer]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsEmployer, IsJobOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()
