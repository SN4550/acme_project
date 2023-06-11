from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['first_name', 'last_name', 'birthday']
        widget = {'birthday': forms.DateInput(attrs={'type': 'date'})}
