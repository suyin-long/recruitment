import debug_toolbar
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf import settings
from django.urls import include, path

from jobs import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # 职位列表
    url(r'^joblist/$', views.joblist, name='joblist'),
    # 管理员创建 HR 账号的页面:
    path('create_hr_user/', views.create_hr_user, name='create_hr_user'),
    # 职位详情
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    # url(r'^job/<int:job_id>/$', views.detail, name='detail'),
    # 提交简历
    url(r'^resume/add/$', views.ResumeCreateView.as_view(), name='resume-add'),
    path(r'resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    # 首页自动跳转到职位列表
    url(r'^$', views.joblist, name='name'),
    # sentry路由
    path('sentry-debug/', trigger_error),
    # path('__debug__/', include(debug_toolbar.urls)),
]


# debug_toolbar
# if settings.DEBUG:
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
