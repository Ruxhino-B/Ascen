# Generated by Django 4.1.5 on 2023-01-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackhours', '0003_workday_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='day',
            field=models.CharField(blank=True, default='empty', max_length=15, null=True),
        ),
    ]
