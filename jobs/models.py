from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))
JobTypes = [
    (0, '技术类'),
    (1, '产品类'),
    (2, '运营类'),
    (3, '设计类'),
    (4, '市场营销类')
]
Cities = [
    (0, '北京'),
    (1, '上海'),
    (2, '深圳'),
    (3, '杭州'),
    (4, '广州')
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='职位类型')
    job_name = models.CharField(max_length=250, blank=False, verbose_name='职位名称')
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name='工作地点')
    job_responsibility = models.TextField(max_length=1024, verbose_name='职位职责')
    job_requirement = models.TextField(max_length=1024, verbose_name='职位要求')
    creator = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = '职位列表'

    def __str__(self):
        return self.job_name
