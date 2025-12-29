from rest_framework.permissions import BasePermission

class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_employer


class IsApplicationOwnerOrJobOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.applicant == request.user or
            obj.job.company.owner == request.user
        )
