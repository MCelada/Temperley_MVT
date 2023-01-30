from django.urls import path

from shirts.views import create_shirt, list_shirts, update_shirt, ShirtDeleteView

urlpatterns = [
    path('create-shirt/', create_shirt),
    path('list-shirts/', list_shirts, name='list_shirts'),
    path('update_shirt/<int:pk>/', update_shirt),
    path('delete_shirt/<int:pk>/', ShirtDeleteView.as_view(template_name='shirts/delete_shirt.html'), name='delete_shirt'),
]