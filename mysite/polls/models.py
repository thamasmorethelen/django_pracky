from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DatetimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.Cascade)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
