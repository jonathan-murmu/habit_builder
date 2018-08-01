from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from habit.forms import AddHabitForm


class HabitView(TemplateView):
    template_name = 'habit/list_habit.html'


class AddHabitView(LoginRequiredMixin, TemplateView):
    template_name = 'habit/add_habit.html'

    def get_context_data(self, **kwargs):
        """Add extra data in context."""
        form = AddHabitForm()

        context = super(AddHabitView, self).get_context_data(**kwargs)
        context.update({
            'form_header': 'Add New Habit',
            'form': form
        })

        return context

    def post(self, request, *args, **kwargs):
        form = AddHabitForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            habit = form.save(commit=False)
            habit.created_by = request.user
            habit.save()
            form.save_m2m()
        else:
            print(form.errors)

        return redirect('habit')