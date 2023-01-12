from django.urls import path

from coachs.views import create_coach, list_coachs

urlpatterns = [
    path('create-coach/', create_coach),
    path('list-coachs/', list_coachs),
]