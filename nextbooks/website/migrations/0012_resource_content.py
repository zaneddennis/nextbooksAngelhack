# Generated by Django 2.0.6 on 2018-07-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20180714_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]