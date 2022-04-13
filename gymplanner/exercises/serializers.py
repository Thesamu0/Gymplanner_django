from .models import Exercise
from rest_framework import serializers

class ExerciseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id','name','difficulty_rating','description']

class ExerciseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name','difficulty_rating','description']