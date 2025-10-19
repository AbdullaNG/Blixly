from django.urls import path
from blog import views

urlpatterns = [
    path("", views.PostListView.as_view(), name='blog-home'),
    path("about/", views.about, name='blog-about'),
]
