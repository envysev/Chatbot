from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('logout/', views.logout_view, name='logout'),
    path('disconnect/github/', views.disconnect_github, name='disconnect_github'),  # <-- This line is required
]
