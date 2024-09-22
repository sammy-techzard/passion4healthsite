# Generated by Django 5.1.1 on 2024-09-10 13:36

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_whyprojectsection_more_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_team', wagtail.fields.StreamField([('block_title', 0), ('title', 0), ('members', 8)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': True}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {'max_num': 1, 'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'max_length': 255, 'required': True}), 3: ('wagtail.blocks.EmailBlock', (), {'required': True}), 4: ('wagtail.blocks.CharBlock', (), {'min_length': 10, 'required': True}), 5: ('wagtail.blocks.URLBlock', (), {'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'max_length': 20, 'required': True}), 7: ('wagtail.blocks.StructBlock', [[('picture', 1), ('first_name', 2), ('second_name', 2), ('email', 3), ('phone', 4), ('linkedIn', 5), ('role', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {'max_num': 5})})),
            ],
            options={
                'verbose_name': 'Our Team',
                'verbose_name_plural': 'Our Team',
            },
        ),
    ]
