from django.urls import path

from habit.views import HabitView, AddHabitView

urlpatterns = [
    path('', HabitView.as_view(), name='habit'),
    path('add_habit/', AddHabitView.as_view(), name='add_habit'),
]