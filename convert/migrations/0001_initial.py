# Generated by Django 5.0.2 on 2024-02-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoosePatternModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(choices=[('cyrillic', 'Cyrillic'), ('latin', 'Latin')], max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChoosePatternModelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(choices=[('cyrillic', 'Cyrillic'), ('latin', 'Latin')], max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='uploads/%Y/%m')),
            ],
        ),
    ]
