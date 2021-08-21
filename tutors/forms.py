from django import forms
from .models import Tutor

class TutorSelectForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('city', 'subject')

    def __init__(self, subject=None, city=None):
        super().__init__()
        if subject and city:
            self.fields['subject', 'city'].queryset = Tutor.objects.filter(city=city, subject=subject)