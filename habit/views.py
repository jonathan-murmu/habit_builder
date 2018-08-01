import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from habit.forms import AddHabitForm
from habit.models import Habit, Log


class HabitView(LoginRequiredMixin, TemplateView):
    template_name = 'habit/list_habit.html'

    def get(self, request, *args, **kwargs):
        """Displays the habits."""
        queryset = Habit.objects.filter(created_by=request.user)
        return render(
            request, self.template_name,
            self.get_context_data(
                queryset=queryset,
            )
        )


class AddHabitView(LoginRequiredMixin, TemplateView):
    template_name = 'habit/add_habit.html'

    def get(self, request, *args, **kwargs):
        """Displays the habits."""
        form = AddHabitForm()


        return render(
            request, self.template_name,
            self.get_context_data(
                form=form,
                form_header='Add New Habit'
            )
        )

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


class RecordHabitDone(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        habit_pk = self.kwargs['pk']

        try:
            habit_obj = Habit.objects.get(pk=habit_pk)
        except:
            messages.error(request, 'Habit not found!')
            return redirect('habit')
        Log.objects.create(habit=habit_obj, user=request.user)

        messages.success(request, 'Successfully updated Habit')
        return redirect('habit')
