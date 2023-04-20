import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200) #tipo de dato para un atributo
    pub_dat = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_publiched_recently(self):
        return self.pub_dat >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choise_text