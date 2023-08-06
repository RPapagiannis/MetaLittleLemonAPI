from rest_framework import permissions
 

class CanManageMenuItemPermission(permissions.BasePermission):
    message = 'You do not have the permission to manage menu items.'

    def has_permission(self, request, view):
        # If user is a superuser or has the specific permission, grant access
        return request.user.is_superuser or request.user.has_perm('LittleLemonAPI.add_menuitem')
    
class CanManageUsers(permissions.BasePermission):
    message = 'You do not have the permission to manage users.'

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.has_perm('auth.add_user')
    
