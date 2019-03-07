from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    question_type = models.CharField(max_length=100)
    def __str__(self):
        return "{}: {}".format(self.__class__, self.question_text)


class SingleChoice(Question):
    question_type = "SingleChoice"
    choices = models.TextField()
    answer = models.IntegerField()
    parent_link=True

class MultipleChoice(Question):
    question_type = "MultipleChoice"
    choices = models.TextField()
    answer = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    parent_link=True

class FillInBlank(Question):
    question_type = "FillInBlank"
    answer = models.TextField(max_length=100)
    parent_link=True

class TrueOrFalse(Question):
    question_type = "TrueOrFalse"
    answer = models.BooleanField()
    parent_link=True

class ShortAnswerQuestion(Question):
    question_type = "ShortAnswerQuestion"
    answer = models.TextField()
    parent_link=True

