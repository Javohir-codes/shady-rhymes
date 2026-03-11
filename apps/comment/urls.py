from django.urls import path
from .views import add_comment, product_comments

urlpatterns = [
    path('product/<int:product_id>/comments/', product_comments, name='product_comments'),
    path('product/<int:product_id>/comment/add/', add_comment, name='add_comment'),
]