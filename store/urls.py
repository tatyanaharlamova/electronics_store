from rest_framework.routers import SimpleRouter

from store.apps import StoreConfig
from django.urls import path

from store.views import (
    ProductViewSet, LinkListAPIView, LinkCreateAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, LinkDestroyAPIView,
)

app_name = StoreConfig.name

router = SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", LinkListAPIView.as_view(), name="link_list"),
    path("create/", LinkCreateAPIView.as_view(), name="link_create"),
    path("<int:pk>/", LinkRetrieveAPIView.as_view(), name="link_retrieve"),
    path("<int:pk>/update/", LinkUpdateAPIView.as_view(), name="link_update"),
    path("<int:pk>/delete/", LinkDestroyAPIView.as_view(), name="link_delete"),
] + router.urls
