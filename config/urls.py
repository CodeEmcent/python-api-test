from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # API url
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # Apps url
    path("home/", include("core.urls")),
    path("account/", include("accounts.urls")),
    path("payment/", include("payments.urls")),
    path("product/", include("products.urls")),
]
