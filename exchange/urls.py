from django.urls import path
from .views import pending_list

urlpatterns = [
    path('pending/list/', pending_list),
]
