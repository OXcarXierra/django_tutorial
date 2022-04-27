from django.http import HttpResponseForbidden
from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()  # request를 보낸 유저와 실제 유저가 같은지 판단
        return func(request, *args, **kwargs)

    return decorated
