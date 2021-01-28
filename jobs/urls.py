from django.conf.urls import url
from jobs import views

urlpatterns = [
    # 职位列表
    url(r'^joblist/$', views.joblist, name='joblist'),
]
