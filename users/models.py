from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

# Pledge model
class Pledge(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # The amount pledged
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # The user making the pledge
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # Assuming you have a Project model
    date = models.DateTimeField(auto_now_add=True)  # Date and time when the pledge was made

    def __str__(self):
        return f'{self.user.username} pledged {self.amount} to {self.project.name}'

# If you want to add a Project model, here is an example:
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
