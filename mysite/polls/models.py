from django.db import models

# Create your models here.
'''
A model is the single, definitive source of truth about your data.
It contains the essential fields and behaviors of the data you’re storing.
Django follows the DRY Principle.
The goal is to define your data model in one place and automatically derive things from it
'''
#Each Question can have multiple Choices
class Question(models.Model):
    question_text = models.CharField(max_length=200) # Each field is represented by an instance of a Field class – e.g., CharField
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
