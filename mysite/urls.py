from django.urls import path, include
from agenda.urls import urlpatterns as get_url
urlpatterns = [
    path("", include(get_url)),
]
