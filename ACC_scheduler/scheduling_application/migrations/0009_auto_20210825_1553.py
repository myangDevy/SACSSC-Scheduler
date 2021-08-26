# Generated by Django 3.2.5 on 2021-08-25 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_application', '0008_alter_volunteer_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='availability',
        ),
        migrations.AddField(
            model_name='day',
            name='day_of_month',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='volunteer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Days', to='scheduling_application.volunteer'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='additional_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
