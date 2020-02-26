from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('news/', views.news, name='news'),
    path('files/', views.files, name='files'),
    #path('<str:student_id>/', views.detalle_Estudiante, name='detalle_Estudiante')
    
]