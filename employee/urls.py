from django.conf.urls import patterns, include, url
from employee import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hrms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',            views.dashboard.as_view(), name='dashboard'),
    url(r'^requisition$', views.requisition.as_view(), name='requisition'),
    url(r'^candidates$', views.candidates.as_view(), name='candidates'),
    url(r'^intw-schedules$', views.intw_schedules.as_view(), name='candidates'),
    url(r'^employees$', views.employees.as_view(), name='employees'),
    url(r'^leave$', views.leave.as_view(), name='leave'),
    url(r'^apply_leave$', views.apply_leave.as_view(), name='apply_leave'),
)