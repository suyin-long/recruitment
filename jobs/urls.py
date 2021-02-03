from django.conf.urls import url
from jobs import views

urlpatterns = [
    # 职位列表
    url(r'^joblist/$', views.joblist, name='joblist'),
    # 职位详情
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    # 提交简历
    url(r'^resume/add/$', views.ResumeCreateView.as_view(), name='resume-add'),
    # 首页自动跳转到职位列表
    url(r'^$', views.joblist, name='name'),
]
