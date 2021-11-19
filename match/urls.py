from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register('group', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('joined_member/', JoinMember.as_view()),
    path('match_list/', MatchList.as_view()),
    path('filter_match/', FilterMatch.as_view()),
]