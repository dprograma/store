from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItemForSupplierApiView, ItemViewSet, SuppliersForItemApiView, SupplierViewSet

router = DefaultRouter()
router.register(r"items", ItemViewSet)
router.register(r"suppliers", SupplierViewSet)

urlpatterns = [
    path(
        "items/<int:pk>/suppliers/",
        SuppliersForItemApiView.as_view(),
        name="items_supplier",
    ),
    path(
        "supplier/<int:pk>/items/",
        ItemForSupplierApiView.as_view(),
        name="suppliers_item",
    ),
    path("", include(router.urls)),
]
