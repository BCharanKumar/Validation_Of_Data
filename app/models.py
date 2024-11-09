from django.db import models

# Create your models here.

from django import forms
from django.core.validators import *


def check_for_char(data):

    if not data[0].isalpha():
        raise forms.ValidationError('error here..')
def check_for_email(value):
    if not value[0].isalpha():
        raise forms.ValidationError('eror')

class Student(models.Model):
    sname=models.CharField(max_length=125,validators=[check_for_char,MinLengthValidator(6)])
    sid=models.IntegerField(primary_key=True)
    semail=models.EmailField(validators=[check_for_email,])
    phone=models.CharField(max_length=10,default='9346096771',validators=[RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname
    
    
    