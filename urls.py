import os.path
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from registration.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main_page),
    
    #(r'^manage/$', manage)
    (r'^manage/addsession$', add_session)
    # Example:
    # (r'^slrf/', include('slrf.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
