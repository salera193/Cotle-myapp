from django import forms
from  .models import Recruit, Apply

class RecForm(forms.ModelForm):
    
    class Meta:
        model = Recruit
        fields = ('title', 'content')
'''
class AppForm(forms.ModelForm):
    
    class Meta:
        model = Apply
        fields = ('owner','recruit')
'''