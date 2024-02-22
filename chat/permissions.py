from rest_framework.permissions import BasePermission


class IsParticipantsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.admin or request.user in obj.participants.all()


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_active or request.user.is_staff)