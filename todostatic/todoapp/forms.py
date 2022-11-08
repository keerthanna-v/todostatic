from django import forms
from todoapp.models import todomodel
class todoform(forms.ModelForm):
    class Meta:
        model=todomodel
        fields='__all__'