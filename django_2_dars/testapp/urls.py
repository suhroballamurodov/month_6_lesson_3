from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('test', test),
    path('download',download)
]