from django.urls import path

from shirts.views import create_shirt, list_shirts

urlpatterns = [
    path('create-shirt/', create_shirt),
    path('list-shirts/', list_shirts),
]