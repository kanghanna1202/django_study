import json
import urllib

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_open_api import my_settings


@csrf_exempt
@api_view(['GET'])
def movie_list(request):

    ServiceKey = my_settings.SERVICE_KEY

    url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2"\
          + "&ServiceKey=" + ServiceKey + "&listCount=3"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        return Response(dict, status=status.HTTP_200_OK)
    else:
        return Response(rescode, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def search_movie(request):

    ServiceKey = my_settings.SERVICE_KEY
    search = urllib.parse.quote(request.title)

    url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2" \
          + "&ServiceKey=" + ServiceKey + "&query" + search

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        return Response(dict, status=status.HTTP_200_OK)
    else:
        return Response(rescode, status=status.HTTP_400_BAD_REQUEST)
