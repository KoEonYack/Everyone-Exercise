from django.contrib import admin
from django.shortcuts import redirect
from django.template.context_processors import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ad_post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/remove', views.post_remove, name='post_remove'),

    path('<int:post_pk>/comments/new/', views.comment_new, name='comment_new'),
    path('<int:post_pk>/comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
]

