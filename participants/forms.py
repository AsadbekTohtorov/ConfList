from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["full_name", "country", "position", "workplace", "academic_degree", "thesis_title"]
