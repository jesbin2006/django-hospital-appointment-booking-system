from django import forms
from django.contrib.auth.models import User

class registeration(forms.ModelForm):

    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )

    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }