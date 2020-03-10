from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    answered = models.BooleanField(default=False)

class Answer(models.Model):
    answer_text = models.TextField()
    helpful_answer = models.BooleanField(default=False)

class Comment(models.Model):
    comment_text = models.TextField()