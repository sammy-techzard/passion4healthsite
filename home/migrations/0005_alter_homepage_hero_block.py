# Generated by Django 5.1.1 on 2024-09-07 15:55

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_hero_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_block',
            field=wagtail.fields.StreamField([('templated', 8)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'help_text': 'Write the main display text', 'required': True}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 2: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add sub text to the main Hero Text', 'required': False}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'Text to display on the button', 'max_length': 50, 'required': True}), 4: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'The page the button links to', 'required': True}), 5: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('primary', 'Primary'), ('transparent', 'Transparent')], 'help_text': 'Choose the color of the button'}), 6: ('wagtail.blocks.StructBlock', [[('button_text', 3), ('button_link', 4), ('button_color', 5)]], {}), 7: ('wagtail.blocks.ListBlock', (6,), {'help_text': 'Add more call-to-action buttons', 'max_num': 5, 'min_num': 1, 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('hero_text', 0), ('bg_img', 1), ('sub_text', 2), ('cta_buttons', 7)]], {})}, help_text='Block for Hello Section', null=True),
        ),
    ]
