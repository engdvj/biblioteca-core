from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def debug_auth(request):
    return Response({
        'is_authenticated': request.user.is_authenticated,
        'user': request.user.username if request.user.is_authenticated else None,
        'token_header': request.META.get('HTTP_AUTHORIZATION'),
    })
