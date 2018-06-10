from django.urls import path
from first.views import index, start, status

urlpatterns = [
    path('', index),
    path('start/', start),
    path('status/', status),
]
