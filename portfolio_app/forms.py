from django.forms.widgets import Textarea
from .models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(attrs={'cols': 20, 'rows': 3}),
        }
