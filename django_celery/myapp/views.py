import json
import urllib

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from django_celery import my_settings


@csrf_exempt
def movie_list(request):

    ServiceKey = my_settings.SERVICE_KEY

    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json)" \
          + "?key=" + ServiceKey

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        return Response(dict, status=status.HTTP_200_OK)
    else:
        return Response(rescode, status=status.HTTP_400_BAD_REQUEST)
