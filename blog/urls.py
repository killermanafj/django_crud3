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
    path('profile/', views.get_profile, name='profile'),
    path('drafts/', views.post_draft, name="post_draft"),
    path('posts/<int:pk>/info/', views.post_info, name="post_info"),
    path('posts/<int:pk>/publish/', views.post_publish, name="post_publish"),
]
