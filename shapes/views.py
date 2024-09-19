# myapp/views.py

from django.http import JsonResponse, HttpResponseBadRequest
from .rectangle import Rectangle

def rectangle_info(request):
    length = request.GET.get('length')
    width = request.GET.get('width')

    try:
        length = int(length)
        width = int(width)
        
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers")
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid 'length' or 'width' parameter")
    
    try:
        rect = Rectangle(length=length, width=width)
    except (ValueError, TypeError) as e:
        return HttpResponseBadRequest(str(e))

    data = list(rect)
    return JsonResponse(data, safe=False)
