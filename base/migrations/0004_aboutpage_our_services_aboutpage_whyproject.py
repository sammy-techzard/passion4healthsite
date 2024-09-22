# Generated by Django 5.1.1 on 2024-09-18 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_aboutpage_delete_basicpage'),
        ('snippets', '0011_alter_donationsfundsandscholars_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='our_services',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.ourservice'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='whyproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.whyprojectsection'),
        ),
    ]
