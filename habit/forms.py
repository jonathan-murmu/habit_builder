from django.forms import ModelForm

from habit.models import Habit


class AddHabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'