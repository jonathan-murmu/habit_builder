from django.urls import path

from habit.views import HabitView, AddHabitView, RecordHabitDone

urlpatterns = [
    path('', HabitView.as_view(), name='habit'),
    path('add_habit/', AddHabitView.as_view(), name='add_habit'),
    path('record_habit_done/<int:pk>/', RecordHabitDone.as_view(), name='record_habit_done'),
]