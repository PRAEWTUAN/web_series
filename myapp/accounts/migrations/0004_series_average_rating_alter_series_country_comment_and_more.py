# Generated by Django 5.0.6 on 2024-09-25 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_series_cover_image_series_cover_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='series',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.series')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='accounts.series')),
            ],
        ),
    ]
