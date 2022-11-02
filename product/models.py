from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from yun import settings
from .choice import *
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="카테고리")

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        db_table = "카테고리"
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리"


class Product(models.Model):
    name = models.CharField(verbose_name="이름", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="카테고리", related_name='product_category')
    image = models.ImageField(verbose_name="사진", upload_to='static/img/product', blank=False)
    date = models.DateTimeField(verbose_name='일시', default=timezone.now)
    place = models.TextField(verbose_name='장소', default='')
    price = models.IntegerField(verbose_name="가격", default='')
    summary = models.TextField(verbose_name="요약", default='')
    about = models.TextField(verbose_name="설명", default='')
    eg_summary = models.TextField(verbose_name="영어 요약", default='')
    eg_about = models.TextField(verbose_name="영어 설명", default='')

    def __str__(self):
        return '{}, {}'.format(self.category, self.name)

    class Meta:
        db_table = "상품"
        verbose_name = "상품"
        verbose_name_plural = "상품"


class Order(AbstractBaseUser):
    user_id = models.CharField(max_length=17, verbose_name="아이디")
    password = models.CharField(max_length=256, verbose_name="비밀번호", default='')
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True)
    hp = models.IntegerField(verbose_name="핸드폰번호", null=True)
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    grade = models.CharField(choices=COUNT_CHOICES, max_length=18, verbose_name="인원", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=3)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='결제일', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'auth'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "주문"
        verbose_name = "주문"
        verbose_name_plural = "주문"