# Generated by Django 3.1.5 on 2022-11-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=100, verbose_name='카테고리 이름'),
        ),
        migrations.AddField(
            model_name='category',
            name='eg_category_name',
            field=models.CharField(default='', max_length=100, verbose_name='카테고리 영어 이름'),
        ),
    ]
