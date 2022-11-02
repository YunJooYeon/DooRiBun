# Generated by Django 3.1.5 on 2022-11-01 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20221102_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_joined',
            new_name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='auth',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='order',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='order',
            name='level',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='password',
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품'),
        ),
    ]