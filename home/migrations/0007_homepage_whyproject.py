# Generated by Django 5.1.1 on 2024-09-10 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_our_services'),
        ('snippets', '0004_alter_whyprojectsection_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='whyproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.whyprojectsection'),
        ),
    ]
