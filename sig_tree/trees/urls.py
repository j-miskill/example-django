from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name  = "trees-home"),
    path("about/", views.about, name = "trees-about")
]