from django.urls import path
from . import views

urlpatterns = [
    # CustomUser Views
    path('users/', views.CustomUserList.as_view(), name='customuser-list'),  # List and create users
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),  # Detail view for a user
    
    # Auth Token
    path('auth-token/', views.CustomAuthToken.as_view(), name='custom-auth-token'),  # Custom authentication token

    # Pledge Views
    path('pledge/', views.CreatePledge.as_view(), name='create-pledge'),  # Create a pledge

    # Project Views
    path('projects/', views.ProjectList.as_view(), name='project-list'),  # List and create projects
]
