# Generated by Django 2.0.6 on 2018-07-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180714_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='courseTag',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CourseNumberTag',
        ),
    ]