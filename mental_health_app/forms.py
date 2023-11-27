# mental_health_app/forms.py
from django import forms
from .models import Missionary

class MissionaryForm(forms.ModelForm):
    class Meta:
        model = Missionary
        fields = ['name', 'rating', 'message']