from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only autheticated users can view list.
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Other logged in users can view 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only owner has write permission.
        return request.user == obj.author