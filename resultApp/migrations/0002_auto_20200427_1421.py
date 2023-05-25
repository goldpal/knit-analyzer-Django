# Generated by Django 2.1.11 on 2020-04-27 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resultApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carryover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20)),
                ('subject_code', models.CharField(max_length=20)),
                ('obtain_marks', models.FloatField(default=0)),
                ('year_of_result', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('dinank', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('year_of_result', models.CharField(max_length=20)),
                ('obtain_marks', models.FloatField(default=0)),
                ('total_marks', models.FloatField(default=10.0)),
                ('status', models.CharField(max_length=20)),
                ('carry_over_status', models.IntegerField()),
                ('dinank', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together={('roll', 'semester')},
        ),
    ]
