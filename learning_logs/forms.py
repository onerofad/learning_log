from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ctrate a form to add a new topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    """create entry for each Topic"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : 'Entry:'}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}