# accounts/middleware.py
import json


class EnforceJSONContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/signin/' or request.path == '/signup/':
            # TODO: 此接口暂时写死content_type，避免客户端通过curl命令传递--data-raw数据无法处理
            request.META['CONTENT_TYPE'] = 'application/json'
        return self.get_response(request)
