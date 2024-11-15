from django.urls import path
from .views import *

urlpatterns = [
    path("api/category/", CategoryViewSet.as_view, name="category"),
    path("api/brand/", BrandViewSet.as_view, name="brand"),
]
