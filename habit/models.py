from django.contrib.auth.models import User
from django.db import models

from habit import constants


class UserTime(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Habit(UserTime):
    HABIT_TYPE_CHOICES = (
        (constants.HOURLY, 'hourly'),
        (constants.DAILY, 'daily'),
        (constants.WEEKLY, 'weekly')
    )
    WEEKDAY_CHOICES = (
        (constants.MONDAY, 'monday'),
        (constants.TUESDAY, 'tuesday'),
        (constants.WEDNESDAY, 'wednesday'),
        (constants.THURSDAY, 'thursday'),
        (constants.FRIDAY, 'friday'),
        (constants.SATURDAY, 'saturday'),
        (constants.SUNDAY, 'sunday')
    )
    habit = models.CharField(max_length=255)
    habit_type = models.CharField(choices=HABIT_TYPE_CHOICES, max_length=1)
    hourly_interval = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    habit_time = models.TimeField(null=True, blank=True)
    week_day = models.CharField(
        choices=WEEKDAY_CHOICES, null=True, blank=True, max_length=1)
    # Streak is counted on daily and weekly basis only. Any hourly
    # update is also recorded as daily streak one.
    daily_streak_count = models.PositiveIntegerField(default=0)


class Journal(UserTime):
    journal_description = models.TextField()
    how_was_the_day = models.PositiveSmallIntegerField(default=0)


class Log(models.Model):
    completed_at = models.DateTimeField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Streak(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streak_count = models.PositiveIntegerField(default=0)
