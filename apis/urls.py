from django.urls import path

from .views import TopicAPIView

urlpatterns = [
    path('', TopicAPIView.as_view(), name='book_api'),
]