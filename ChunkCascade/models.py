from django.db import models
from django.utils import timezone
from users import User
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField()
    favorited = models.BooleanField()
    owner = models.ForeignKey('User', related_name='owned_questions', on_delete=models.DO_NOTHING)

class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField()
    helpful_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    favorited = models.BooleanField()
    owner = models.ForeignKey('User', related_name='owned_questions', on_delete=models.DO_NOTHING)

class Comment(models.Model):
    comment_text = models.TextField()