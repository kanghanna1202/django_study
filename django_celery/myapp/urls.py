from django.urls import path

from myapp import views

urlpatterns = [
    path('list/', views.movie_list)
]
