from django.conf.urls import patterns, include, url
from registration.backends.default.views import RegistrationView
from .forms import ExRegistrationForm

"""
    http://johnparsons.net/index.php/2013/06/28/creating-profiles-with-django-registration/
"""

urlpatterns = patterns('',
                       url(r'^register/$',
                           RegistrationView.as_view(form_class=ExRegistrationForm),
                           name='registration_register'),
)