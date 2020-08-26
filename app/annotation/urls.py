from django.urls import path

from . import views

app_name = 'annotation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:annotation_id>/', views.detail, name='detail'),
#     path('<int:annotation_id>/summary/', views.summary, name='summary'),
# ]
