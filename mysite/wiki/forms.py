from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    search_content= forms.BooleanField(
        required=False,
        label="Search content?",
        #widget=forms.CheckboxInput(attrs={'class':'form-control'})
    )
    
