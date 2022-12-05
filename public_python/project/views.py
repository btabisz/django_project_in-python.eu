from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.views import generic
from project.forms import EditProfileForm


def register_complete(request):
    messages.add_message(request, messages.INFO, 'Click the link in the email to activate your account!')
    return HttpResponseRedirect('/')


def activation_complete(request):
    messages.add_message(request, messages.INFO, 'Your account is active, you can log in now!')
    return HttpResponseRedirect('/')


def homepage(request):
    template_name = 'home.html'
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class UserUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/update_user.html'
    success_url = '/accounts/update_user'
    success_message = "User updated!"

    def get_object(self):
        return self.request.user


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = '/accounts/update_user'
    success_message = "Password has been changed!"


