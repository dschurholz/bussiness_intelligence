import os

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # API v1
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
)

# We need to serve the static file even on release because the Django tests
# run on release even though DEBUG is set to FALSE (!)
# In reality, when we deploy this in nginx, we are adding a directive to alias
# these files to an isolated folder (dashboard_app) so when the user hits these
# urls nginx will serve them before gunicorn has a chance to get them

urlpatterns += (
    url(r'^dashboard/?$', RedirectView.as_view(url='/dashboard/index.html'), name='dashboard'),
    url(r'^dashboard/(?P<path>.*)$', 'django.views.static.serve',
        {
            'document_root': os.path.join(settings.SITE_ROOT,
                                          'frontend/app/dashboard_app')
        }))

# Serve static files (only for development)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
