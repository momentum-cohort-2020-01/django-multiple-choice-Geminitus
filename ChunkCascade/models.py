from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=256)

class Answer(models.Model):
    answer_text = models.TextField()

class Comment(models.Model):
    comment_text = models.TextField()