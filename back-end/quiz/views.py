from rest_framework import generics

from .serializers import QuizSerializer, QuizDetailSerializer, AnswerQuizSerializer, RecordSerializer
from .models import Quiz, QuizAnswer


class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class RetrieveQuiz(generics.RetrieveAPIView):
    serializer_class = QuizDetailSerializer
    queryset = Quiz.objects.all()

class AnswerList(generics.ListAPIView):
    serializer_class = AnswerQuizSerializer

    def get_queryset(self):
        question = self.kwargs['q_pk']

        return QuizAnswer.objects.all().filter(question=question)

class CreateRecord(generics.CreateAPIView):
    serializer_class = RecordSerializer
