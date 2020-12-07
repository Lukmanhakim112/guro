from django.contrib import admin

from .models import Quiz, Question, QuizAnswer, Score, Record

models =  [Quiz, Question, QuizAnswer, Score, Record]

for m in models:
    admin.site.register(m)
