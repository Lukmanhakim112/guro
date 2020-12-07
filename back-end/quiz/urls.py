from django.urls import path
from .views import QuizList, RetrieveQuiz, AnswerList, CreateRecord

urlpatterns = [
    path('quiz/', QuizList.as_view()),
    path('quiz/record/', CreateRecord.as_view()),
    path('quiz/<int:pk>/', RetrieveQuiz.as_view()),
    path('quiz/<int:pk>/<int:q_pk>/', AnswerList.as_view()),
]
