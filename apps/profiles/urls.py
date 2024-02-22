from rest_framework.routers import DefaultRouter
from .views import CompanyPViewSet, UserPViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('user_profiles', UserPViewSet)
router.register('company_profiles', CompanyPViewSet)

urlpatterns = [
    path('', include(router.urls)),
]