# Generated by Django 3.1.7 on 2021-03-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0002_student_convinence_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Convinence_fee',
            field=models.FloatField(default=100, null=True),
        ),
    ]
