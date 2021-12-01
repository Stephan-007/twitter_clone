from django import forms
from .models import Twitt

class Tweetform(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = '__all__'