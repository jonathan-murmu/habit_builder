from django.urls import path

from habit.views import HabitView

urlpatterns = [
    path('', HabitView.as_view(), name='habit'),
]