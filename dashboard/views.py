from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from dashboard.forms import SignUpForm, SignInForm


class HomeView(TemplateView):
    template_name = "dashboard/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name,
            self.get_context_data(
                user=request.user,
                active_link='dashboard'
            )
        )


class SignUpView(TemplateView):
    template_name = "dashboard/signup.html"

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(
            request, self.template_name,
            self.get_context_data(
                form=form,
                active_link='signup'
            )
        )

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')


class SignInView(TemplateView):
    template_name = 'dashboard/signin.html'

    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(
            request, self.template_name,
            self.get_context_data(
                form=form,
                active_link='signin'
            )
        )

    def post(self, request, *args, **kwargs):
        form = SignInForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            auth_user = authenticate(
                username=data['username'], password=data['password']
            )
            if auth_user.is_active:
                login(request, auth_user)
                messages.success(request, 'Successfully logged in as {0}'.format(auth_user))
                return redirect('dashboard')
            else:
                messages.error(request,
                               'Wrong username or password'.format(
                                    auth_user))
                return redirect('signin')
        else:
            print(form.errors)

        return redirect('signin')
