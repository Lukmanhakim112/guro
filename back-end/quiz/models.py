from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Quiz(models.Model):
    quiz_name = models.CharField('Quiz Name', max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quiz_name}"


class Question(models.Model):
    question_text = models.TextField('Question')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="question")
    img = models.ImageField('Image', upload_to='img_question', null=True, blank=True)

    def __str__(self):
        return f"{self.question_text}"

class QuizAnswer(models.Model):
    answer_text = models.TextField()
    is_right = models.BooleanField('Right Asnwer', default=False)
    img = models.ImageField('Image', upload_to='img_answer', null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")

    def __str__(self):
        return f"{self.answer_text}"

class Record(models.Model):
    participant = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    question = models.OneToOneField(Question, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(QuizAnswer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.participant} answer {self.question} on {self.quiz}"

class Score(models.Model):
    participant = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    quiz = models.OneToOneField(Quiz, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.participant} - {self.quiz} get {self.score}"
