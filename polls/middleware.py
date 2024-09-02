

def simple_middleware(get_response):
    def middleware(request):
        request.my_custom_attr = 'wasd'
        response = get_response(request)
        


        return response

    return middleware

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.customatr = 'hello!'
        response = self.get_response(request)
        return response