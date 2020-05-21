from django import forms
from  .models import Recruit

class RecForm(forms.ModelForm):
    
    class Meta:
        model = Recruit
        fields = ('title', 'content')