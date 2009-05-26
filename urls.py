from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mytickets/', include('mytickets.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ticket.views.homepage', name='homepage'),
    url(r'^event/(?P<event_id>\w+)/$', 'ticket.views.event_detail', name='event_detail'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    )

