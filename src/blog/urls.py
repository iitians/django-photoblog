from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage-view'),
    path('post/<int:pk>', views.PhotoView.as_view(), name='photo-detail'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tag/<str:tag>/', views.TagView.as_view(), name='tag-view'),
    path('<slug:slug>/', views.PageView.as_view(), name='page-view'),
]
