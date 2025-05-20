from rest_framework import permissions

from employer.models import Employer


class IsOwnerOfEmployer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user