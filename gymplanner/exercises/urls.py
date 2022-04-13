from django.urls import path
from .views import (ExerciseCreateAPIView,ExerciseDeleteAPIView,ExerciseListAPIView,ExerciseUpdateAPIView)
urlpatterns = [
    path('getExercises',ExerciseListAPIView.as_view(), name='list'),
    path('postExercises/',ExerciseCreateAPIView.as_view(), name='create'),
    path('putExercises/<str:id>/',ExerciseUpdateAPIView.as_view(), name='update'),
    path('deleteExercises/<str:id>/',ExerciseDeleteAPIView.as_view(), name='delete'),
]