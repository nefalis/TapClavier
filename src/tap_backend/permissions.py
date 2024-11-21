from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permission pour vérifier que l'utilisateur est le propriétaire de l'objet.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsAdmin(BasePermission):
    """
    Permission pour vérifier que l'utilisateur est un administrateur.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
