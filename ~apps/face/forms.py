from django import forms
from face.models import Face

class FaceForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)  
    about = forms.CharField(widget=forms.Textarea, required=False) 