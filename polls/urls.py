from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),

    path('search/', views.SearchFormView.as_view(), name='search'),
    path('search/<int:maps_id>', views.maps, name='maps'),
    path('csv_upload/', views.csv_upload, name='csv_upload'),
    path('<int:map_pk>/comments/new/', views.comment_new, name='comment_new'),
]
