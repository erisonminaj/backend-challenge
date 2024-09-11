from rest_framework import viewsets, permissions
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from django_filters.rest_framework import DjangoFilterBackend




class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'labels']  # Define the fields you want to filter by

# method to show all tasks for admin users & restrict access to non-admin users
    def get_queryset(self):
        # Check if the user is staff (admin)
        if self.request.user.is_staff:
            # If the user is an admin, return all tasks
            return Task.objects.all()
        else:
            # If the user is not admin, return only their own tasks
            return Task.objects.filter(owner=self.request.user)

    # Set the task owner to the currently logged-in user when creating a task
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  # You can add more fields if needed

    # method to show all labels for admin users & restrict access to non-admin users

    def get_queryset(self):
        # Check if the user is staff (admin)
        if self.request.user.is_staff:
            # If the user is an admin, return all labels
            return Label.objects.all()
        else:
            # If the user is not admin, return only their own labels
            return Label.objects.filter(owner=self.request.user)

    # Set the label owner to the currently logged-in user when creating a label
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
