# Generated by Django 4.1.4 on 2023-01-06 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='email_husband_or_wife',
            new_name='email',
        ),
    ]
