# Generated by Django 3.1.5 on 2022-11-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_order_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='grade',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=18, null=True, verbose_name='개수'),
        ),
    ]
