from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from signup.serializers import PersonSerializer


@permission_classes((AllowAny, ))
@csrf_exempt
@api_view(['GET', 'POST'])
def signup(request):

    serializer = PersonSerializer(data=request.data, required=False)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data, status=201)
    else:
        return HttpResponse(serializer.errors, status=400)

