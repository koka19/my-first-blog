from django.urls import path
from . import views

"""views.post_list das gewünschte Ziel ist,
wenn jemand deine Website über 'http://127.0.0.1:8000/' aufruft
name='post_list' ist der Name der URL, der genutzt wird,
um die View zu identifizieren
"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
