from django.http.response import JsonResponse
from rest_framework import status
from api.services import get_goods_info
from rest_framework.decorators import api_view


@api_view(['POST'])
def test(request):
    file = request.FILES.get('file')
    code = request.POST.get('code')
    if not file and not code or code and file:
        return JsonResponse(
            {'detail': 'please send file or code'},
            status=status.HTTP_400_BAD_REQUEST)
    result = get_goods_info(file, code)
    if len(result) == 1:
        return JsonResponse(result[0].__dict__, safe=False)
    return JsonResponse([goods.__dict__ for goods in result], safe=False)
