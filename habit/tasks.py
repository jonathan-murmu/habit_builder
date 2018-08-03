from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone
from fcm_django.models import FCMDevice

from habit.models import Habit


@periodic_task(run_every=(crontab(hour='*/1', minute=0)), name="check_and_send_notification")
def check_and_send_notification():
    """Check for habits every hour and send notifications."""
    now = timezone.now()
    daily_weekly_devices = FCMDevice.objects.filter(user__habit__habit_time__hour=now.hour + 1)
    for device in daily_weekly_devices:
        title = device.user.habit.habit
        message = 'Don\'t forget to complete this habit at {0}.'.format(
            device.user.habit.habit_time)

        # for daily habits.
        if device.user.habit.habit_type == '2':
            print (title, message)
            try:
                daily_weekly_devices.send_message(title, message)
            except Exception as e:
                print(e)

        # for weekly habits.
        if device.user.habit.habit_type == '3' and device.user.habit.week_day.filter(week_day=now.weekday() + 1).exists():
            print(title, message)
            try:
                daily_weekly_devices.send_message(title, message)
            except Exception as e:
                print(e)

    # for interval habits.
    hourly_habits = Habit.objects.filter(habit_type='1')

    for habit in hourly_habits:
        # difference between current hour by created time's hour, divided by the
        # hourly interval gives zero as remainder then it should be sent now.
        # 1 hour is added to current hour to send the notification one hour
        # before.
        if ((now.hour + 1) - habit.created_at.hour) % habit.hourly_interval == 0:
            hourly_device = FCMDevice.objects.filter(user__habit=habit)
            title = 'Hourly Reminder'
            message = habit.habit
            print(title, message)
            try:
                hourly_device.send_message(title, message)
            except Exception as e:
                print(e)


