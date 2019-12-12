from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = modelsCharField(max_length=200)
    pub_date = models.DateTimeField('pub date')


class Choice(models.Model):
    question = models.Foeignkey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

