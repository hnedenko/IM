from rest_framework import serializers
from .models import Exercise, Difficulty, Chapter


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
