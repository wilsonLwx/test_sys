from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserInfo(AbstractUser):
    """
    用户信息
    """
    user_level = (
        ('1', '一级'),
        ('2', '二级'),
        ('3', '三级'),
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    level = models.CharField(max_length=10, choices=user_level, default='1', verbose_name='用户级别')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
