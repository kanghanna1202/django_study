from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Account
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import json
import bcrypt
import jwt
from django.conf import settings


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def sign_up(request):
    payload = json.loads(request.body)
    try:
        user = Account.objects.create(
            id=payload["id"],
            name=payload["name"],
            password=bcrypt.hashpw(payload["password"].encode("UTF-8"),
                                   bcrypt.gensalt()).decode("UTF-8")
        )
        return JsonResponse({'success': user.id}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def sign_in(request):
    payload = json.loads(request.body)
    try:
        if Account.objects.filter(id=payload["id"]).exists():
            check_user = Account.objects.get(id=payload["id"])
            if bcrypt.checkpw(payload["password"].encode('UTF-8'), check_user.password.encode('UTF-8')):
                token = jwt.encode({"user": check_user.id}, settings.SECRET_KEY, algorithm='HS256').decode('UTF-8')
                return JsonResponse({"token": token}, safe=False,
                                    status=status.HTTP_200_OK)
            return JsonResponse({'error': 'wrong input'}, safe=False,
                                status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'error': 'wrong input'}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except KeyError as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
