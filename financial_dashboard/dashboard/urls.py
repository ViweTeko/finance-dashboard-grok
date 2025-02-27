from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetClassViewSet, FinancialDataViewSet

router = DefaultRouter()
router.register(r'asset-classes', AssetClassViewSet)
router.register(r'financial-data', FinancialDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
]