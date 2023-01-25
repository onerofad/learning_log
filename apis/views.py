from django.shortcuts import render

from rest_framework import generics

from  learning_logs.models import Topic

from .serializers import TopicSerializer

class TopicAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer