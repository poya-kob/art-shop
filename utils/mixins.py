from django.http import HttpResponseRedirect


class UserNotLoggedInMixin:
    """Verify that the current user is not be authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to="/")
        return super().dispatch(request, *args, **kwargs)
