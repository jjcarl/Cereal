from django import forms
from django.core.validators import RegexValidator
from main.models import Cereal


class CerealSearchForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z\s]+$', "Please Type Letters")
    name = forms.CharField(required=True, initial='Smacks',
                                                  validators=[alphanumeric],
                                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    manufacturer = forms.CharField(required=True, initial='Kellogs',
                                   validators=[alphanumeric],
                                   widget=forms.TextInput(attrs={'class': "form-control"}))


class CreateCerealForm(forms.ModelForm):
    class Meta:
        model = Cereal
