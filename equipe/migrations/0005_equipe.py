# Generated by Django 4.1 on 2022-08-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0004_rename_others_streamer_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=128)),
                ('twitch', models.CharField(blank=True, max_length=256)),
                ('youtube', models.CharField(blank=True, max_length=256)),
                ('twitter', models.CharField(blank=True, max_length=256)),
                ('instagram', models.CharField(blank=True, max_length=256)),
                ('tiktok', models.CharField(blank=True, max_length=256)),
                ('other', models.CharField(blank=True, max_length=256)),
                ('pp', models.ImageField(blank=True, null=True, upload_to='equipes')),
            ],
        ),
    ]
