# Generated by Django 3.0.8 on 2020-07-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200707_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateField(auto_now_add=True, verbose_name='发布时间'),
        ),
    ]