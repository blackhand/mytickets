from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    )

# mytickets app urls
urlpatterns += patterns('ticket.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^(?P<category>\w+)/$', 'event_list', name='event_list'),
    url(r'^event/(?P<event_id>\w+)/$', 'event_detail', name='event_detail'),
    )

# static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    )

