from .models import Profile
from forms import UserRegistrationForm


def user_created(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    data = Profile(user=user)
    data.gender = form.data["gender"]
    data.save()

from registration.signals import user_registered
user_registered.connect(user_created)