# Generated by Django 3.2 on 2022-01-31 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_phone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_postcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deault_town_or_city',
            new_name='default_town_or_city',
        ),
    ]
