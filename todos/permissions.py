from rest_framework import permissions


class IsAuthorOrIsNotPrivate(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only autheticated users can view list of todos that are not private.
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Other logged in users can view todo details that are not private
        if request.method in permissions.SAFE_METHODS and obj.private == False:
            return True
        
        # Only owner has write permission.
        return request.user == obj.author