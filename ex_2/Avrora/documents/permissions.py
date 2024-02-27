from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class IsAuthorOrSuperuser(AccessMixin):
    """
    Permission to check if the user is the author of the object or a superuser.
    """

    permission_denied_message = "You don't have permission to view"

    def dispatch(self, request, *args, **kwargs):
        author = self.get_object().user

        if not request.user.is_superuser:
            if request.user != author:
                raise PermissionDenied(self.permission_denied_message)

        return super().dispatch(request, *args, **kwargs)
