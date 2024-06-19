# main/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label=_('שם'),
        help_text=_('הכנס את שמך המלא'),
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
    email = forms.EmailField(
        label=_('אימייל'),
        help_text=_('הכנס את כתובת האימייל שלך'),
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
    message = forms.CharField(
        label=_('הודעה'),
        help_text=_('כתוב את ההודעה שלך כאן'),
        widget=forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
