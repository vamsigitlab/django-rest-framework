from rest_framework.permissions import BasePermission
from authentication.models import User

class IsUserAuthenticated(BasePermission):
    def has_instace(self, request, view):
        return isinstance(request.user, User)