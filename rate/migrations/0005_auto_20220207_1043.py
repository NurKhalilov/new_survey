# Generated by Django 3.2.5 on 2022-02-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_alter_rating_salesperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='phone',
        ),
        migrations.AddField(
            model_name='rating',
            name='price',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
