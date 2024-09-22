# Generated by Django 5.1.1 on 2024-09-12 20:47

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('snippets', '0011_alter_donationsfundsandscholars_options'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_block', wagtail.fields.StreamField([('templated', 0)], blank=True, block_lookup={0: ('wagtail.blocks.StructBlock', [[]], {})}, help_text='Block for Hello Section', null=True)),
                ('donations_funds_and_scholars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.donationsfundsandscholars')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
