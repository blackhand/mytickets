from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# fix for bug in django admin urls in Django 1.1 beta
admin.site.root_path = '/admin/'

urlpatterns = patterns('',
    # Admin urls
    (r'^admin/', include(admin.site.urls)),
    # auth urls
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),

    # Registration urls
    (r'^accounts/', include('registration.urls')),
    )

# mytickets app urls
urlpatterns += patterns('ticket.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^(?P<category>\w+)/$', 'event_list', name='event_list'),
    url(r'^event/(?P<event_id>\w+)/$', 'event_detail', name='event_detail'),
    url(r'^event/(?P<presentation_id>\w+)/(?P<zone_id>\w+)/sucess/$', 'buy_sucess', name='buy_sucess'),
    )

# static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    )

