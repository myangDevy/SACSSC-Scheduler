# Generated by Django 3.2.5 on 2021-08-24 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_application', '0007_auto_20210823_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='availability',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduling_application.availability'),
        ),
    ]