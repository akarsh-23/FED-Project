# Generated by Django 3.1.7 on 2021-03-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0009_auto_20210314_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='PHONE',
        ),
    ]
