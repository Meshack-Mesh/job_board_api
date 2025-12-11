from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsEmployer(BasePermission):
    """
    Allows access only to employer users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employer


class IsCompanyOwner(BasePermission):
    """
    Allows access only to the owner of the company.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
