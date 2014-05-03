from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

import views

v1_urlpatterns = patterns('',
    # Login
    # url(r'^login/?$', views.Login.as_view(), name='login'),

    # Views
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
    url(r'^event/(?P<event_id>(\d+))/?$',
        views.EventDetail.as_view(),
        name='event-detail'),

    # Time Queries
    url(r'^speed-infringements/max-year/?$',
        views.MaxYearSpeedInfringementQuery.as_view(),
        name='max-year-query'),
    url(r'^speed-infringements/max-day/(?P<year>(\d+))/(?P<month>(\d+))/?$',
        views.MaxDaySpeedInfringementQuery.as_view(),
        name='max-day-query'),
    url(r'^speed-infringements/max-month/(?P<year>(\d+))/?$',
        views.MaxMonthSpeedInfringementQuery.as_view(),
        name='max-month-query'),
    url(r'^speed-infringements/max-fifteenth/(?P<year>(\d+))/(?P<month>(\d+))/?$',
        views.MaxFifteenthSpeedInfringementQuery.as_view(),
        name='max-fifteenth-query'),

    # Region Queries
    url(r'^speed-infringements/max-region/?$',
        views.SpeedInfringementByRegionQuery.as_view(),
        name='max-region-query'),
    url(r'^speed-infringements/max-province/(?P<region>([\w_]+))/?$',
        views.SpeedInfringementByProvinceQuery.as_view(),
        name='max-province-query'),
    url(r'^speed-infringements/max-district/(?P<region>([\w_]+))/(?P<province>([\w_]+))/?$',
        views.SpeedInfringementByDistrictQuery.as_view(),
        name='max-district-query'),
    url(r'^speed-infringements/max-road/(?P<region>([\w_]+))/(?P<province>([\w_]+))/(?P<district>([\w_]+))/?$',
        views.SpeedInfringementByRoadQuery.as_view(),
        name='max-road-query'),
)

urlpatterns = patterns('',
    # API v1
    url(r'^v1/', include(v1_urlpatterns)),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
