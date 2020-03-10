from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    answer_text = models.TextField()
    helpful_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_text = models.TextField()