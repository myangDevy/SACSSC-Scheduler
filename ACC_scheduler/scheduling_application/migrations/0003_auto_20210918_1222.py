# Generated by Django 3.2.5 on 2021-09-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_application', '0002_auto_20210917_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveystatus',
            name='survey_id',
        ),
        migrations.AddField(
            model_name='surveystatus',
            name='date_sent',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]