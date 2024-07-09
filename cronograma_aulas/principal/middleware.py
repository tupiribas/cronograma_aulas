from django.utils.deprecation import MiddlewareMixin
from .models import AccessLog


class LogRequestMiddleware(MiddlewareMixin):
    def processos_request(self, request):
        if not request.path.startswith('/static/'):
            # Save access details to the database
            AccessLog.objects.create(
                ip_address=request.META.get('REMOTE_ADDR'),
                path=request.path
            )
