from rest_framework import permissions


class OnlyAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)

    def __str__(self):
        return 'У вас недостаточно прав для выполнения данного действия.'
