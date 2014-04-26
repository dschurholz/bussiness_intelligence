from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

import views

v1_urlpatterns = patterns('',
    url(r'^customers/?$',
        views.CustomerList.as_view(),
        name='customer-list'),
    url(r'^customers/(?P<customer_id>(\d+))/?$',
        views.CustomerDetail.as_view(),
        name='customer-detail'),
    url(r'^customer-units/?$',
        views.DimCustomerUnitList.as_view(),
        name='customer-unit-list'),
    url(r'^customer-units/(?P<unit_id>(\d+))/?$',
        views.DimCustomerUnitDetail.as_view(),
        name='customer-unit-detail'),
    url(r'^references/?$',
        views.DimReferenceList.as_view(),
        name='reference-list'),
    url(r'^references/(?P<ref_id>(\d+))/?$',
        views.DimReferenceDetail.as_view(),
        name='reference-detail'),
    url(r'^speed-infringements/?$',
        views.SpeedInfringementList.as_view(),
        name='speed-infringement-list'),
    url(r'^speed-infringements/(?P<spinf_id>(\d+))/?$',
        views.SpeedInfringementDetail.as_view(),
        name='speed-infringement-detail'),
    url(r'^region/?$',
        views.RegionList.as_view(),
        name='region-list'),
    url(r'^region/(?P<region_id>(\d+))/?$',
        views.RegionDetail.as_view(),
        name='region-detail'),
    url(r'^time/?$',
        views.TimeList.as_view(),
        name='time-list'),
    url(r'^time/(?P<time_id>(\d+))/?$',
        views.TimeDetail.as_view(),
        name='time-detail'),
    url(r'^event/?$',
        views.EventList.as_view(),
        name='event-list'),
    url(r'^event/(?P<event_id>(\d+))/?$',
        views.EventDetail.as_view(),
        name='event-detail'),
)

urlpatterns = patterns('',
    # API v1
    url(r'^v1/', include(v1_urlpatterns)),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
