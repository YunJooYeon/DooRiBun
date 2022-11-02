# Generated by Django 3.1.5 on 2022-11-01 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='카테고리')),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리',
                'db_table': '카테고리',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('image', models.ImageField(upload_to='static/img/product', verbose_name='사진')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='일시')),
                ('place', models.TextField(default='', verbose_name='장소')),
                ('price', models.IntegerField(default='', verbose_name='가격')),
                ('summary', models.TextField(default='', verbose_name='요약')),
                ('about', models.TextField(default='', verbose_name='설명')),
                ('eg_summary', models.TextField(default='', verbose_name='영어 요약')),
                ('eg_about', models.TextField(default='', verbose_name='영어 설명')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category', verbose_name='카테고리')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': '상품',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=128, null=True, verbose_name='이메일')),
                ('hp', models.IntegerField(null=True, verbose_name='핸드폰번호')),
                ('name', models.CharField(max_length=8, null=True, verbose_name='이름')),
                ('grade', models.CharField(choices=[('-', '-'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=18, null=True, verbose_name='개수')),
                ('level', models.CharField(choices=[('3', 'Lv3_미인증사용자'), ('2', 'Lv2_인증사용자'), ('1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=3, max_length=18, verbose_name='등급')),
                ('auth', models.CharField(max_length=10, null=True, unique=True, verbose_name='인증번호')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='결제일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': '주문',
            },
        ),
    ]