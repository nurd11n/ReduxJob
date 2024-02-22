from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, ErCodeViewSet, ForumViewSet, CompanyPostViewSet, CompanyVacancyViewSet, DitailCompanyPostViewSet, DitailCompanyVacancyViewSet, DitailUserPostViewSet

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('er_code', ErCodeViewSet)
router.register('forum', ForumViewSet)
router.register('comp_vacancy', CompanyVacancyViewSet)
router.register('comp_post', CompanyPostViewSet)
router.register('add_comp_post', DitailCompanyPostViewSet)
router.register('add_comp_vac', DitailCompanyVacancyViewSet)
router.register('add_user_post', DitailUserPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
