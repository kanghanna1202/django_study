from django.db import models


class Movie(models.Model):
    movieCd = models.IntegerField
    movieNm = models.CharField(max_length=50)
    repGenreNm = models.CharField(max_length=20)
