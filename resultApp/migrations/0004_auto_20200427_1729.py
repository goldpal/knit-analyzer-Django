# Generated by Django 2.1.11 on 2020-04-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultApp', '0003_auto_20200427_1726'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carryover',
            unique_together={('roll', 'year_of_result', 'semester')},
        ),
    ]
