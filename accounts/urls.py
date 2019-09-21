from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUsersView.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
]