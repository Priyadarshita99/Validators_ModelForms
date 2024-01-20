from django.db import models

# Create your models here.
from django.core import validators
from django import forms

def validate_for_a(data):
    if data.lower()[0]=='a':
        raise forms.ValidationError('a_Error')
    
class Student(models.Model):
    Sname=models.CharField(max_length=50,validators=[validate_for_a])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10)

    def __str__(self):
        return self.Sname