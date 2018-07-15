from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("resource/<int:pk>", views.ResourceDetailView.as_view(), name="resource-detail"),
    path("find/", views.find, name="find"),
    path("feed/", views.feed, name="feed"),
    path("quiz/", views.quiz, name="quiz"),
]
