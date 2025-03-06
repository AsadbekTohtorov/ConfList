from django.urls import path
from .views import register_participant, participants_list

urlpatterns = [
    path("register/", register_participant, name="register_participant"),
    path("list/", participants_list, name="participants_list"),
]
