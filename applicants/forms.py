from django import forms
from .models import Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'phone', 'position', 'resume_url', 'resume_file', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'resume_url': forms.URLInput(attrs={'class': 'form-control'}),
            'resume_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

