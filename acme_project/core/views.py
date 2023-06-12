from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    return render(request=request,
                  template_name='core/404.html',
                  status=404)


def csrf_failure(request: HttpRequest, reason='') -> HttpResponse:
    return render(request=request,
                  template_name='core/403csrf.html',
                  status=403)
