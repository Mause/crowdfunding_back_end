from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),  # Lists all projects
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),  # Retrieves a specific project
    path('pledges/', views.PledgeList.as_view()),  # Lists all pledges
    path('pledges/create/', views.create_pledge),  # POST request to create a pledge (use function-based view)
]
