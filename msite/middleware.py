from .models import Msworks
from django.http import HttpResponse
class MyMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        server = Msworks.objects.first()
        servering = Msworks.objects.count()
        if  '/admin/' in request.path or servering == 1:
            return response
        elif servering > 1:
            return HttpResponse(server.report)
        else:
            return HttpResponse("Django Server is Running")




