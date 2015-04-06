from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from api.views.employee import UserViewSet, EmployeeViewSet, LeaveViewSet, ApplyLeaveViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'leave', LeaveViewSet)
router.register(r'apply_leave', ApplyLeaveViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hrms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^web/', include('employee.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
