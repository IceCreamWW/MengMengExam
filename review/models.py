from django.db import models
from django.contrib.auth.models import User
from study.models import Question

class UserWrongAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    error_cnt = models.IntegerField()
