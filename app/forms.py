from django import forms
from django.core import validators
def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')
def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

class CompanyForm(forms.Form):
    cname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(5)])
    cmanager=forms.CharField(validators=[validate_for_a])
    clocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')    
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError('emails are not same')