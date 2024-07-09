from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from .models import AccessLog


class LogRequestMiddleware(MiddlewareMixin):
    def processos_request(self, request):
        if not request.path.startswith('/static/'):
            # Save access details to the database
            AccessLog.objects.create(
                ip_address=request.META.get('REMOTE_ADDR'),
                path=request.path
            )


class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and request.path == settings.LOGIN_REDIRECT_URL:
            return redirect('redireciona_apos_login')
        return response
