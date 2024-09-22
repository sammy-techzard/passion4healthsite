# Generated by Django 5.1.1 on 2024-09-10 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_ourteam'),
        ('snippets', '0009_becomevolunteersection_theblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='callforvolunteer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.becomevolunteersection'),
        ),
    ]
