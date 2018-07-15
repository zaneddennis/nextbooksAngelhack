
from django import forms
from django.core.exceptions import ValidationError
from .models import Resource


class FindForm(forms.Form):
    level = forms.ChoiceField(choices=Resource.LEVEL_CHOICES)
    subject = forms.ChoiceField(choices=Resource.SUBJECT_CHOICES)
    course = forms.CharField(max_length=50, required=False, label="Course Name")
    courseNumber = forms.IntegerField(required=False, label="Course Number")
    keywords = forms.CharField(required=False)
