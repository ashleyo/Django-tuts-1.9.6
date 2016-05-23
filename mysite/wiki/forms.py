from django import forms
from django.forms import ModelForm
from .models import UserFileUpload

class SearchForm(forms.Form):
    text = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    search_content= forms.BooleanField(
        required=False,
        label="Search content?",
        )
    
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload' ]