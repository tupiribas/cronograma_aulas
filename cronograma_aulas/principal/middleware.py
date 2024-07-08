from .models import AccessLog


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Save access details to the database
        AccessLog.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
            path=request.path
        )

        # Process the request
        response = self.get_response(request)

        return response
