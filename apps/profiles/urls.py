from django.urls import path
from .views import (AgentListAPIView,GetProfileAPIView,TopAgentsListAPIView,UpdateProfileAPIView)

urlpatterns = [
    path("me/",GetProfileAPIView.as_view(),name="get_profile ")
]