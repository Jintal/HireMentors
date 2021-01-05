# Generated by Django 3.1.4 on 2021-01-05 12:11

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=260)),
                ('last_name', models.CharField(max_length=260)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/youtubers/%Y/%m')),
                ('video_url', models.CharField(max_length=260)),
                ('description', ckeditor.fields.RichTextField()),
                ('city', models.CharField(max_length=260)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(choices=[('Solo', 'Solo'), ('Small', 'Small'), ('Large', 'Large')], max_length=260)),
                ('camera_type', models.CharField(choices=[('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Sony', 'Sony'), ('Red', 'Red'), ('Fuji', 'Fuji'), ('Panasonic', 'Panasonic'), ('Other', 'Other')], max_length=260)),
                ('category', models.CharField(choices=[('Physics', 'Physics'), ('Web Development', 'Web Development'), ('Android Development', 'Android Development'), ('Chemistry', 'Chemistry'), ('Maths', 'Maths'), ('Commerce', 'Commerce'), ('Banking', 'Banking'), ('Software Development', 'Software Development'), ('CA/CS Exams', 'CA/CS Exams'), ('Arts', 'Arts'), ('Sciene', 'Sciene'), ('General Science', 'General Science'), ('Other', 'Other')], max_length=260)),
                ('subs_count', models.CharField(max_length=260)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]