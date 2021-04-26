import json
import urllib

from django.http import HttpResponse, JsonResponse

from django_celery import my_settings


def movie_list(self):
    service_key = my_settings.SERVICE_KEY

    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json" \
          + "?key=" + service_key

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))['movieListResult']['movieList']
        return HttpResponse(status=201)
    else:
        return JsonResponse({"message": rescode}, status=400)
