from django import forms
from .models import ContactMe


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'ph_no', 'msg')
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }),

            'ph_no': forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Your phone number"
            }),

            'msg': forms.Textarea(attrs={
                "class": "form-control",
                # 'cols': 80,
                # 'rows': 20,
                "placeholder": "write your message",
            }),
        }
