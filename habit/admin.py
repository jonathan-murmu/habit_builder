from django.contrib import admin

from habit.models import Habit, Journal, Log, Streak, Week

admin.site.register(Habit)
admin.site.register(Week)
admin.site.register(Journal)
admin.site.register(Log)
admin.site.register(Streak)