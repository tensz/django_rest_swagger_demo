from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_rest_swagger_demo.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^api-docs/', include('rest_framework_swagger.urls')),
                       url(r'^demo/', include('demo.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
