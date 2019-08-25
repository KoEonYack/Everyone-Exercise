from django.urls import path
from . import views

app_name='object_board'

urlpatterns = [
    path('csv_upload_food/', views.csv_upload_food, name='csv_upload_food'),
    path('csv_upload_mets/', views.csv_upload_mets, name='csv_upload_mets'),

    path('exercise/', views.FoodPostListView.as_view(), name='exercise'),
    path('score/', views.FoodSearchFormView.as_view(), name='score'),

    #path('exercise/result/',views.result, name="result"),
    # path('list/', views.PostListView.as_view(), name='list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/remove', views.post_remove, name='post_remove'),
    path('<int:post_pk>/comments/new/', views.comment_new, name='comment_new'),
]
