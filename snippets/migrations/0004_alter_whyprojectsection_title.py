# Generated by Django 5.1.1 on 2024-09-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_whyprojectsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whyprojectsection',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Main Title'),
        ),
    ]
