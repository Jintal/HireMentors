# Generated by Django 3.1.4 on 2021-01-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='photo',
            field=models.ImageField(upload_to='media/mentors/%Y/%m'),
        ),
    ]
