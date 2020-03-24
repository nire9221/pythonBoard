from django import forms
from .models import Article, Job, Event

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'