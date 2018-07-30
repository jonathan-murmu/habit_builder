from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "dashboard/home.html"


class SignUpView(TemplateView):
    template_name = "dashboard/signup.html"
    form = UserCreationForm()

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name,
            self.get_context_data(
                form=self.form,
            )
        )
