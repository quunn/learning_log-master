# Generated by Django 2.1.2 on 2018-10-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
