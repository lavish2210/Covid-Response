# Generated by Django 3.2 on 2021-05-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fever', models.BooleanField(default=False)),
                ('cough', models.BooleanField(default=False)),
                ('Tiredness', models.BooleanField(default=False)),
                ('other_symptoms', models.IntegerField(default=0)),
                ('breathing_problem', models.BooleanField(default=False)),
                ('chest_pain', models.BooleanField(default=False)),
            ],
        ),
    ]
