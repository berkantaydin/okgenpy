from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm, AvatarForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        af = AvatarForm(request.POST, request.FILES, prefix='avatar')
        if uf.is_valid() and af.is_valid():
            user = uf.save(commit=False)
            user.is_active = True
            user.set_password(user.password)
            user.save()
            author = af.save(commit=False)
            author.user = user
            author.save()
            # TODO: Confirmation mail will send
            messages.success(request, _('Sign Up Success!'))
            messages.info(request, _('Please go to your inbox and read the activation mail'))
            return redirect(reverse('pageHome'))
    else:
        uf = UserForm(prefix='user')
        af = AvatarForm(prefix='avatar')

    return render(request, 'okgen_accounts/signup.html', dict(userForm=uf, avatarForm=af), )