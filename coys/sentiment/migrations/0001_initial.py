# Generated by Django 4.1 on 2022-08-28 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=300)),
                ('body', models.TextField(max_length=1000)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('body', models.TextField(max_length=1000)),
                ('user', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment.post')),
            ],
        ),
    ]
