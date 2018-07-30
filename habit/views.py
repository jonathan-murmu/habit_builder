from django.shortcuts import render
from django.views.generic import TemplateView


class HabitView(TemplateView):
    template_name = 'habit/list_habit.html'