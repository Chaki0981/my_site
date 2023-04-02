from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path("posts", views.AllPostsView.as_view(), name='posts-page'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("posts/<slug:slug>", views.ShowPostView.as_view(),
        name='post-detail-page'),
]
