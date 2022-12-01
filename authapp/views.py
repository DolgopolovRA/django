from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib import messages
from authapp.models import User
from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mainapp:main_page")


class CustomLogoutView(LogoutView):
    pass


class EditView(UserPassesTestMixin, UpdateView):

    model = get_user_model()
    form_class = CustomUserChangeForm

    def test_func(self):
        return True if self.request.user.pk == self.kwargs.get("pk") else False

    def get_success_url(self):
        return reverse_lazy("authapp:edit", args=[self.request.user.pk])
