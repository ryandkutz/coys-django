# Generated by Django 4.1 on 2022-08-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0004_user_sentiment_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment.user'),
        ),
    ]
