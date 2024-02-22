from .views import ResumeView, ResumeDetailView, OtherResumeViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('other_resume', OtherResumeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('resume/', ResumeView.as_view()),
    path('resume/<int:pk>/', ResumeDetailView.as_view()),
    # path('employer_retrieve_resume/<slug:slug>/', EmployerResumeRetrieveView.as_view()),

]

