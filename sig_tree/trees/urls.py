from django.urls import path

from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name  = "trees-home"),
    path("trees/<int:pk>/", PostDetailView.as_view(), name  = "post_detail"),
    path("trees/new/", PostCreateView.as_view(), name  = "post_create"),
    path("trees/<int:pk>/update/", PostUpdateView.as_view(), name  = "post_update"),
    path("trees/<int:pk>/delete/", PostDeleteView.as_view(), name  = "post_delete"),
    path("about/", views.about, name = "trees-about")
]