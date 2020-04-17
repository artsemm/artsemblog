from django.urls import path, include

from .views import PostListView, PostSingleView, PostTitlesView

urlpatterns = [
    path('all-titles', PostTitlesView.as_view(), name='post_titles'),
    path('<slug:slug>', PostSingleView.as_view(), name='post_single'),
    path('tag/<slug:tag_slug>', PostListView.as_view(), name='post_list_tag'),
    path('', PostListView.as_view(), name='post_list'),
]
