from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap

admin.autodiscover()

handler500 = "ossum2013.views.server_error"

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
