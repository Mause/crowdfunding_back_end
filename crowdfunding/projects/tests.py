from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Project, Pledge

class PledgeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.project = Project.objects.create(
            title="Test Project",
            description="Test description",
            goal=5000,
            is_open=True,
            owner=self.user,
        )

    def test_create_pledge_unauthenticated(self):
        url = "/pledges/"
        data = {"amount": 50, "project": self.project.id, "anonymous": False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_pledge_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = "/pledges/"
        data = {"amount": 50, "project": self.project.id, "anonymous": False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

