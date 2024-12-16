from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Import the status module
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

# Project views
class ProjectList(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED  # Use status from rest_framework
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  # Use status from rest_framework
        )

class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  # Use status from rest_framework
        )

# Pledge views
class PledgeList(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the project exists in the request data
            project_id = request.data.get("project")
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return Response({"detail": "Project does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Associate the pledge with the current user (supporter)
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED  # Use status from rest_framework
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  # Use status from rest_framework
        )

class PledgeDetail(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  # Use status from rest_framework
        )

# New PledgeCreate view for handling pledge creation with authentication
class PledgeCreate(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can make a pledge

    def post(self, request):
        # Initialize the PledgeSerializer with the data from the request
        serializer = PledgeSerializer(data=request.data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Associate the pledge with the current authenticated user (supporter)
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the pledge data with status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors with status 400
