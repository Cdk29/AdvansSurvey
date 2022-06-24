from django.urls import path

from . import views

app_name = 'cve'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:pk>/', views.DetailView.as_view(), name='detail'),
    path('archives/', views.ArchivesView.as_view(), name='archives'),
]
