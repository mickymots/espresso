from django import forms 
  
class OwnIntakeForm(forms.Form): 
    name = forms.CharField(label="name",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )
    title = forms.CharField(label="title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )
    description = forms.CharField(label="Description",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )
    available = forms.CharField(label="available",
                           widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})) 
    proof_file = forms.FileField() 