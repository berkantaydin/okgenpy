from django.conf.urls import patterns, include, url
from registration.backends.default.views import RegistrationView
from .forms import UserRegistrationForm

urlpatterns = patterns('',
    url(r'^register/$', RegistrationView.as_view(form_class=UserRegistrationForm)),
    (r'', include('registration.backends.default.urls')),
)