# Generated by Django 5.1.1 on 2024-09-07 15:55

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', wagtail.fields.StreamField([('snippet_title', 0), ('snippet_description', 1), ('services', 6)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Write the title for the Services', 'max_length': 250, 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'Write the something about the Services', 'max_length': 250, 'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'help_text': 'The name of the service ', 'max_length': 50, 'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'A short description of the service!', 'max_length': 250, 'required': True}), 4: ('base.blocks.IconChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.StructBlock', [[('name', 2), ('short_description', 3), ('icon_image', 4)]], {}), 6: ('wagtail.blocks.ListBlock', (5,), {'help_text': 'Add the main services', 'max_num': 3, 'min_num': 1, 'required': False})})),
            ],
        ),
    ]
