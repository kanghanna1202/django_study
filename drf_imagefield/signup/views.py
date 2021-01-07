from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from signup.serializers import PersonSerializer


@permission_classes((AllowAny, ))
@csrf_exempt
@api_view(['GET', 'POST'])
def signup(request):

    # serializer = PersonSerializer(request.data, request.FILES)
    serializer = PersonSerializer(data=request.data, required=False)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse("hello")
    else:
        print(serializer.errors)

    return HttpResponse(serializer.data)

