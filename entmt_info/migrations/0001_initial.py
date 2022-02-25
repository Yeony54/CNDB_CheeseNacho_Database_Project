# Generated by Django 3.2.5 on 2022-02-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('g_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('m_title', models.CharField(max_length=255)),
                ('m_posterPath', models.CharField(max_length=50)),
                ('m_likeCount', models.IntegerField(default=0)),
                ('m_releaseDate', models.DateField()),
                ('m_popularity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('series_id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_title', models.CharField(max_length=255)),
                ('s_posterPath', models.CharField(max_length=50)),
                ('s_likeCount', models.IntegerField(default=0)),
                ('s_firstAirDate', models.DateField()),
                ('s_lastAirDate', models.DateField()),
                ('s_popularity', models.FloatField()),
            ],
        ),
    ]
