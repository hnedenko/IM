from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Chapter
from .serializers import ChapterSerializer


# Create your views here.
class ChapterViewSet(GenericViewSet,
                     mixins.ListModelMixin):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Chapter.objects.all()
        else:
            return Chapter.objects.filter(pk=pk)
