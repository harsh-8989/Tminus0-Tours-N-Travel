# Generated by Django 3.2 on 2021-04-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='location',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='train',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='user',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='train',
        ),
        migrations.AlterField(
            model_name='review',
            name='submissionDate',
            field=models.DateField(),
        ),
    ]