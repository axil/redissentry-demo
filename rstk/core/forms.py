from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

class AuthForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    def clean(self):
        cleaned_data = super(AuthForm, self).clean()
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(_('Incorrect username or password.'))
        return self.cleaned_data


