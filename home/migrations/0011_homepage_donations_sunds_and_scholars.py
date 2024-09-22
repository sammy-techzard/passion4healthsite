# Generated by Django 5.1.1 on 2024-09-10 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_callforvolunteer_homepage_call_for_volunteer'),
        ('snippets', '0011_alter_donationsfundsandscholars_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='donations_sunds_and_scholars',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.donationsfundsandscholars'),
        ),
    ]
