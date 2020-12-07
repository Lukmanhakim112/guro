from rest_framework import serializers

from .models import Quiz, QuizAnswer, Record


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'author']

class QuizDetailSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'author', 'question']

class AnswerQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ['id', 'answer_text', 'img']

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ['participant', 'quiz', 'question', 'answer']
