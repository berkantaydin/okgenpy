from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(),
                                label=_("Username"),
                                error_messages={
                                'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),
                             label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=_("Password (again)"))

    #ADITIONAL FIELDS
    #they are passed to the backend as kwargs and there they are saved
    gender = forms.CharField()

RegistrationForm.base_fields.update(UserRegistrationForm.base_fields)
"""
        http://stackoverflow.com/questions/14764248/extending-the-user-model-with-django-registration
"""