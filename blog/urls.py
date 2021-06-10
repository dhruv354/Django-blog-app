from django.contrib import admin
from django.urls import path, include
# from views import PostView
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='blogHome'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about')
]