# Generated by Django 5.0.3 on 2024-04-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
