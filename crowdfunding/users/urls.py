from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),  # Corrected a typo here
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/create/', views.PledgeCreate.as_view()),  # Ensure this matches
]
