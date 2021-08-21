from django import forms
from .models import Tutor

class TutorSelectForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('city', 'subject')