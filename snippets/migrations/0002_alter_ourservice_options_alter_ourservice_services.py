# Generated by Django 5.1.1 on 2024-09-07 16:31

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourservice',
            options={'verbose_name': 'Our Service', 'verbose_name_plural': 'Our Services'},
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='services',
            field=wagtail.fields.StreamField([('templated', 7)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Write the title for the Services', 'max_length': 250, 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'Write the something about the Services', 'max_length': 250, 'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'help_text': 'The name of the service ', 'max_length': 50, 'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'A short description of the service!', 'max_length': 250, 'required': True}), 4: ('base.blocks.IconChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.StructBlock', [[('name', 2), ('short_description', 3), ('icon_image', 4)]], {}), 6: ('wagtail.blocks.ListBlock', (5,), {'help_text': 'Add the main services', 'max_num': 3, 'min_num': 1, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('snippet_title', 0), ('snippet_description', 1), ('services', 6)]], {})}),
        ),
    ]
