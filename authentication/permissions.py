from rest_framework.permissions import BasePermission
from authentication.models import User

class IsUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, User)
    
class IsUserActive(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active == True
    
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser == True