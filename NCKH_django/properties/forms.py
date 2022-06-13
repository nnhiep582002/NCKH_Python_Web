from dataclasses import fields
from django import forms
from .models import  House, PropertiesEmail, Search, contactMe


        
class PropertiesForm(forms.ModelForm):
    class Meta:
        model = PropertiesEmail
        fields = ["Email"]      

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["UserSearch"]


        
class contactMe_Form(forms.ModelForm):
    class Meta:
        model = contactMe
        fields = ["Name","Email","Number","WriteMessage"]
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Your Name*'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Your Email*'}),
            'Number': forms.TextInput(attrs={'placeholder': 'Your Phone*'}),
            'WriteMessage': forms.Textarea(attrs={'placeholder': 'Messages here*'})
        }