import logging

logger = logging.getLogger(__name__)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log details of the request
        logger.info(f"Access from IP: {request.META.get('REMOTE_ADDR')}, Path: {request.path}")
        
        # Process the request
        response = self.get_response(request)
        
        return response
