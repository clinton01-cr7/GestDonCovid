from django import forms
from Admin.models import Utilisateur
 

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model=Utilisateur
        fields=['nom','email','passwd','role']

class rawUtilisateurForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={
                                                         "placeholder":"your name",
                                                         "class":"form-input"
                                                      }))

    email = forms.CharField(widget=forms.TextInput(attrs={
                                                         "placeholder":"your email",
                                                         "class":"form-input"
                                                      }))



    passwd = forms.CharField(widget=forms.TextInput(attrs={
                                                         "placeholder":"your passwd",
                                                         "class":"form-input"
                                                      }))
    
   



        
