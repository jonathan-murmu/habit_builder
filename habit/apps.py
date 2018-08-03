from django.apps import AppConfig


class HabitConfig(AppConfig):
    name = 'habit'

    def ready(self):
        import habit.signals  # noqa