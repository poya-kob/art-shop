from django.http import HttpResponseRedirect

class UserNotLoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.request.DATA.get('next', '/'))
        return super().dispatch(request, *args, **kwargs)
