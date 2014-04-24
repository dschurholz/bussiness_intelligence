from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

import views

v1_urlpatterns = patterns('',
    url(r'^customers/?$', views.CustomerList.as_view(), name='customer-list'),
)

urlpatterns = patterns('',
    # API v1
    url(r'^v1/', include(v1_urlpatterns)),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
