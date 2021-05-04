from urllib.parse import urlencode, quote_plus, unquote

import bs4
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_open_api import my_settings


@api_view(['GET'])
def movie_list(self):
    service_key = my_settings.SERVICE_KEY

    url = 'http://open.kmrb.or.kr/openapi-data/service/MvResultService/mvResult'

    query_params = '?' + urlencode({quote_plus('ServiceKey'): service_key,
                                   quote_plus('pageNo'): '1', quote_plus('numOfRows'): '2', quote_plus('title'): '1987',
                                   quote_plus('rtNo'): '2017-MF02149', quote_plus('aplcName'): '주식회사 우정필름',
                                   quote_plus('stDate'): '20171201', quote_plus('edDate'): '20171231'})

    get_data = requests.get(url + unquote(query_params))
    soup = bs4.BeautifulSoup(get_data.content, 'html.parser')

    data = soup.find_all('items')

    for i in data:
        print(data)

    return Response(status=status.HTTP_200_OK)
