# Generated by Django 3.1.7 on 2021-03-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionApp', '0004_auto_20210314_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRegistration',
            fields=[
                ('rollno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('class_of_admission', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')], max_length=4)),
                ('marksheet', models.FileField(upload_to='Marksheets/')),
                ('image', models.FileField(upload_to='Image/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]