from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    