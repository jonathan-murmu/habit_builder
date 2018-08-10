from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from habit import constants
from habit.models import Log, Habit, Rewards


@receiver(post_save, sender=Log)
def increase_streak_count(sender, instance, created, **kwargs):
    if created:
        todays_completed_count = sender.objects.filter(
            completed_at__year=timezone.now().year,
            completed_at__month=timezone.now().month,
            completed_at__day=timezone.now().day
        ).count()

        # increase the streak count by one when the user updates a task (i.e.
        # daily or hourly) in a day
        if instance.habit.habit_type in ['1', '2'] and \
                todays_completed_count == 1:
            instance.habit.daily_streak_count += 1
            instance.habit.save()


@receiver(post_save, sender=Habit)
def check_for_streak_and_reward(sender, instance, created, **kwargs):
    """Give rewards on successful creation of streak."""
    if instance.daily_streak_count == 15:
        Rewards.objects.create(user=instance.created_by,
                               badge=constants.BRONZE_BADGE)

    if instance.daily_streak_count == 30:
        Rewards.objects.create(user=instance.created_by,
                               badge=constants.SILVER_BADGE)

    if instance.daily_streak_count == 50:
        Rewards.objects.create(user=instance.created_by,
                               badge=constants.GOLDEN_BADGE)
