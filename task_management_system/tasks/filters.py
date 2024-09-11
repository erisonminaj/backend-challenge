import django_filters
from .models import Task, Label

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['completed', 'labels']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.queryset = self.queryset.filter(owner=user)

class LabelFilter(django_filters.FilterSet):
    class Meta:
        model = Label
        fields = ['name']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.queryset = self.queryset.filter(owner=user)
