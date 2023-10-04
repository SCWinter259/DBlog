from django.urls import path
from .views import Index

urlpatters = [
    path('', Index.as_view(), name='index'),
]