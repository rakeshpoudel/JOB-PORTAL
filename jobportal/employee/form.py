from django import forms
from .models import Employee
class EmployeeCreateForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="First Name")
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Last Name")
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Address")
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),label="Date of Birth")

    class Meta:
        model = Employee
        exclude = ['user',]

class AddSkillForm(forms.ModelForm):
    skillName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    level = forms.IntegerField(widget=forms.IntegerField(attrs={'class':'form-control'}))
