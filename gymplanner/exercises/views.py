from django.shortcuts import render
from .models import Exercise
from .serializers import ExerciseListSerializer,ExerciseCreateSerializer
from rest_framework.generics import (DestroyAPIView,ListAPIView,CreateAPIView,UpdateAPIView)

# Create your views here.

class ExerciseCreateAPIView(CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseCreateSerializer

class ExerciseDeleteAPIView(DestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer
    lookup_field = 'id'

class ExerciseListAPIView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer

class ExerciseUpdateAPIView(UpdateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer
    lookup_field = 'id'