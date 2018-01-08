try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class kankanMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return None


    def process_response(self, request, response):
        return None