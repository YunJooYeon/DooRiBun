# Generated by Django 3.1.5 on 2022-11-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20221102_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]