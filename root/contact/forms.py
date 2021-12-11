from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Contact

class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    captcha = ReCaptchaField(score_threshold=0.5)
    
    class Meta:
        model = Contact
        fields = ('email', )
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent',
                                            'placeholder': 'Введите свой Email'})
        }
        labels = {
            'email': ''
        }
        