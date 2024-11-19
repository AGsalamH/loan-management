from rest_framework import permissions

class RegisterOrIsAuthenticated(permissions.BasePermission):
    '''
    Custom permission to allow user creation without authentication,
    but require authentication for retrieving user information.
    '''

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        # Require authentication for other actions (GET, PUT, DELETE)
        return request.user and request.user.is_authenticated
