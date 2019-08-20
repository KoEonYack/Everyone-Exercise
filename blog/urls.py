from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('main/', views.main, name='main'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/remove', views.post_remove, name='post_remove'),
    path('<int:pk>/', views.post_detail, name='post_detail'),

    path('<int:post_pk>/comments/new/', views.comment_new, name='comment_new'),
    path('<int:post_pk>/comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
]
