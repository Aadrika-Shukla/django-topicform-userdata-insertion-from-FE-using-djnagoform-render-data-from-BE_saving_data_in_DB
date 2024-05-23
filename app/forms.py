from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()


class Webpageform(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.CharField()
    email=forms.CharField()

class Accessform(forms.Form):
    name=forms.ModelChoiceField(queryset=WebPage.objects.all())
    date=forms.DateField()
    author=forms.CharField()
