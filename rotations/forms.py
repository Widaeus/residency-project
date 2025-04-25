# rotations/forms.py
from django import forms
from .models import Rotation

class RotationForm(forms.ModelForm):
    class Meta:
        model = Rotation
        fields = ['service', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date':   forms.DateInput(attrs={'type': 'date'}),
        }
