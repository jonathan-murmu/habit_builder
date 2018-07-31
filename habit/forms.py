from django import forms
from django.forms import ModelForm

from habit.models import Habit, Week


class AddHabitForm(ModelForm):
    # habit_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    week_day = forms.ModelMultipleChoiceField(
        queryset=Week.objects,
        widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Habit
        fields = ['habit','habit_type', 'hourly_interval', 'habit_time',
                  'week_day']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['habit'].widget.attrs.update({'class': 'form-control'})
        self.fields['habit_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['hourly_interval'].widget.attrs.update({'class': 'form-control'})
        self.fields['habit_time'].widget.attrs.update(
            {'class': 'form-control datetimepicker-input',
             'data - target': "#datetimepicker3"}
        )
        self.fields['week_day'].widget.attrs.update({'class': 'form-control'})
