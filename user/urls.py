from django.urls import path
from .views import user_list, register

urlpatterns = [
    path('list/', user_list),
    path('register/', register),
]
