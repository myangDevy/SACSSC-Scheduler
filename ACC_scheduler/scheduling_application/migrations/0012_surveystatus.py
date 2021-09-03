# Generated by Django 3.2.5 on 2021-09-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_application', '0011_alter_volunteer_survey_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(null=True)),
                ('sent', models.BooleanField(default=False)),
                ('survey_id', models.IntegerField(null=True)),
            ],
        ),
    ]
