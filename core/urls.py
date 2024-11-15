from django.urls import path
from .views import (
    home_view,
)

urlpatterns = [
    # core url
    path('', home_view, name='home'),
]