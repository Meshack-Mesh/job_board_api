from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsApplicant, IsApplicationOwnerOrJobOwner

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_employer:
            return Application.objects.filter(job__company__owner=user)
        return Application.objects.filter(applicant=user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsApplicant]
        elif self.action in ['retrieve', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsApplicationOwnerOrJobOwner]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
