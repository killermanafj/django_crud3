from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('posts/new/', views.post_new, name="post_new"),
    path('products', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.get_contacts, name='get_contacts'),
    path('profile/', views.get_profile, name='profile')
]
