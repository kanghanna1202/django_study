from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import CreateView, DetailsView

urlpatterns = {
    path('bucketlists/', CreateView.as_view(), name="create"),
    path('bucketlists/<pk>/', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
