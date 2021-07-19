"""Build a form in Django using ModelForm.

Any page that lets a user enter and submit information on a web page is a form.
"""


from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Define class which inherits from forms.ModelForm."""

    class Meta:
        """Tells Django which models and fields to include."""

        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
