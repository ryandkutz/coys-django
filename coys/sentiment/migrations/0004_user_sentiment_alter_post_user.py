# Generated by Django 4.1 on 2022-08-28 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sentiment',
            field=models.TextField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment.user'),
        ),
    ]
