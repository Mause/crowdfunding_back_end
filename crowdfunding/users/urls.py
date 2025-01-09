from django.urls import path
from . import views

urlpatterns = [
    # CustomUser Views
    path('users/', views.CustomUserList.as_view(), name='customuser-list'),  # List and create users
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),  # Detail view for a user
]
