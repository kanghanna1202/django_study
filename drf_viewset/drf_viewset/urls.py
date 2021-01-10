"""drf_viewset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import PostViewSet

router = routers.DefaultRouter()
router.register('myapp', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

# GET/api/myapp/ 글 리스트 조회
# POST/api/myapp/ 글 추가
# GET/api/myapp/{pk} 글 객체 조회
# PUT/api/myapp/{pk} 글 객체 수정
# DELETE/api/myapp/{pk} 글 객체 삭제
