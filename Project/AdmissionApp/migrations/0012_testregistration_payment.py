# Generated by Django 3.1.7 on 2021-03-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0011_auto_20210315_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='testregistration',
            name='PAYMENT',
            field=models.CharField(blank=True, default='Null', max_length=50),
        ),
    ]
