# Generated by Django 3.1.7 on 2021-03-14 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0008_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='phone',
            new_name='PHONE',
        ),
    ]
