from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('all/', views.view_comments, name='view_comments'),
]