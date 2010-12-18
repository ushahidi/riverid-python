from django import forms
from piston.models import Consumer

class ConsumerForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, initial='Your swift site/app name')
    description = forms.CharField(widget=forms.Textarea, required=True, initial='Tell us a bit about your site/app name')
    url = forms.URLField(required=True, initial='http://')