from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'nisn', 'alamat', 'phone_number', 'kelas', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
        }

        