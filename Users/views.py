from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ProfileForm
from .models import Profile


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")