from rest_framework import permissions


# This is a customized permission for superUser to read and write and
# access to all permission for someone is created this post
# and nobody can see anything when doesn't have any accounted
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                return True
        return obj.author == request.user or request.user.is_superuser
