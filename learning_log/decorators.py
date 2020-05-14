import functools
from django.http import Http404

def is_31029(func):
    """This function helps to identify 31029"""
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.id != 1:
            raise Http404
        return func(request, *args, **kwargs)
    return wrapper



