from django.utils.deprecation import MiddlewareMixin

class XFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-Frame-Options'] = 'ALLOW-FROM https://quickstart-3aa8ad1d.myshopify.com'
        return response

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "frame-ancestors 'self' https://quickstart-3aa8ad1d.myshopify.com"
        return response
