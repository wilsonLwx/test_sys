from datetime import datetime
from django.db import models


# Create your models here.


class InterfaceList(models.Model):
    """
    接口信息
    """
    # uri
    uri = models.CharField(max_length=100, blank=True, null=True, verbose_name='URI')
    # method
    method = models.CharField(max_length=10, blank=True, null=True, verbose_name='请求方式')
    # 接口名称
    title = models.CharField(max_length=10, blank=True, null=True, verbose_name='接口名称')
    # 版本
    version = models.CharField(max_length=10, blank=True, null=True, verbose_name='版本')
    # 描述
    desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='接口描述')
    # 参数
    parameter = models.CharField(max_length=300, blank=True, null=True, verbose_name='参数')
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间')
    # 更新时间
    update_time = models.DateTimeField(default=datetime.now(), verbose_name='更新时间')

    class Meta:
        verbose_name = '接口列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
