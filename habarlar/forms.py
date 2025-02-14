from django import forms
from django.forms import Textarea, EmailInput, TextInput

class MessageForm(forms.Form):
    from_email = forms.EmailField(
        widget=EmailInput(
            attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
    to_email = forms.EmailField(
        widget=EmailInput(
            attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
    subject = forms.CharField(
        widget=TextInput(
            attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
    message = forms.CharField(
        widget=Textarea(
            attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
