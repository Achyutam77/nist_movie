# Generated by Django 5.2.2 on 2025-06-11 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('duration_minutes', models.IntegerField()),
                ('language', models.CharField(choices=[('nepali', 'Nepali'), ('english', 'English'), ('hindi', 'Hindi')], max_length=20)),
                ('cover_image_url', models.URLField()),
                ('trailer_url', models.URLField()),
                ('video_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
    ]
