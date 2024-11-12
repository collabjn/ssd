import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error(f"Error processing request: {str(exception)}")
        return JsonResponse({
            'error': 'An unexpected error occurred',
            'detail': str(exception)
        }, status=500) 