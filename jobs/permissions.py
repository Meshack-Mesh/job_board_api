from rest_framework.permissions import BasePermission

class IsJobOwner(BasePermission):
    """
    Allows access only to the owner of the job (company owner).
    """
    def has_object_permission(self, request, view, obj):
        return obj.company.owner == request.user
