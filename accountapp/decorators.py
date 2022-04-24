from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()  # request를 보낸 유저와 실제 유저가 같은지 판단
        return func(request, *args, **kwargs)

    return decorated
