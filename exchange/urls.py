from django.urls import path
from .views import pending_list, send

urlpatterns = [
    path('pending/list/', pending_list),
    path('send/', send),
]
