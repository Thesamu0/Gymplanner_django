# Generated by Django 4.0.4 on 2022-04-27 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercises.workout'),
        ),
    ]