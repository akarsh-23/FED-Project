# Generated by Django 3.1.7 on 2021-03-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0005_auto_20210314_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testregistration',
            name='rollno',
        ),
        migrations.AddField(
            model_name='testregistration',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
