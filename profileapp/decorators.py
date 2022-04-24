from django.http import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()  # request를 보낸 유저와 실제 유저가 같은지 판단
        return func(request, *args, **kwargs)
    return decorated
