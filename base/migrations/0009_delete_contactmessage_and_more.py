# Generated by Django 5.1.1 on 2024-09-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
        migrations.AddField(
            model_name='contactformsubmission',
            name='responded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactformsubmission',
            name='response_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
