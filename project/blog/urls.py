from django.urls import path
from blog import views

urlpatterns = [
    path("", views.PostListView.as_view(), name='blog-home'),
    path("posts/", views.PostsListView.as_view(), name='posts'),
    path("about/", views.about, name='blog-about'),
    path("post/add", views.PostCreateView.as_view(), name='post-add'),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>", views.post_detail, name='post-detail'),
    path("comment/<int:pk>/delete", views.CommentDeleteView.as_view(), name='comment-delete'),
]
