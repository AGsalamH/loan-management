from rest_framework.permissions import BasePermission, AllowAny


class RegisterOrIsAuthenticated(BasePermission):
    '''
    Custom permission to allow user creation without authentication,
    but require authentication for retrieving user information.
    '''

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        # Require authentication for other actions (GET, PUT, DELETE)
        return request.user and request.user.is_authenticated


class IsLoanProvider(BasePermission):
    '''permission to check if a user is loan provider.'''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsBankPersonnel(BasePermission):
    '''permission to check if a user is a bank personnel.'''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'bank_personnel')


class IsLoanCustomer(BasePermission):
    '''permission to check if a user is a loan customer.'''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'loan_customer')


class CreatePermissionMixin:
    def get_permissions(self):
        if self.action == 'post' or self.action == 'create':
            self.permission_classes = [AllowAny]

        return super().get_permissions()
