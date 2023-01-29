from django.urls import path

from coachs.views import create_coach, list_coachs, update_coach, CoachDeleteView

urlpatterns = [
    path('create-coach/', create_coach),
    path('list-coachs/', list_coachs),
    path('update_coach/<int:pk>/', update_coach),
    path('delete_coach/<int:pk>/', CoachDeleteView.as_view(), name='delete_coach'),
]