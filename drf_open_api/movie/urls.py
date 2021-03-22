from django.urls import path

from movie import views

urlpatterns = [
    path('main/', views.movie_list),
    path('search/', views.search_movie),
]
