from django.db import models
from django.conf import settings
# Create your models here.


class Question(models.Model):
    question_title = models.CharField(max_length=256)
    question_text = models.TextField()
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited = models.BooleanField(default=False)
    question_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       related_name='questions',
                                       on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.question_title}"


class Answer(models.Model):
    question = models.ForeignKey('Question',
                                 related_name='answers',
                                 on_delete=models.CASCADE)
    answer_text = models.TextField()
    helpful_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    favorited = models.BooleanField()
    answer_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.DO_NOTHING)


class Comment(models.Model):
    op = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)