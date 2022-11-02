from django.db import models
# from product.models import Product
#
# class Map(models.Model):
#     name = models.CharField(verbose_name="이름", max_length=255)
#     product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="상품", related_name='product_category')
#     latitude = models.FloatField(verbose_name='위도')
#     longitude = models.FloatField(verbose_name='경도')
#
#     def __str__(self):
#         return '{}'.format(self.name)
#
#     class Meta:
#         db_table = "지도"
#         verbose_name = "지도"
#         verbose_name_plural = "지도"