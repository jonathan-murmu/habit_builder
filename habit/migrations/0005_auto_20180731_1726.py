# Generated by Django 2.0.7 on 2018-07-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_auto_20180731_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='week_day',
            field=models.CharField(blank=True, choices=[(1, 'monday'), (2, 'tuesday'), (3, 'wednesday'), (4, 'thursday'), (5, 'friday'), (6, 'saturday'), (7, 'sunday')], max_length=10, null=True),
        ),
    ]
