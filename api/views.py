from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status

from django.http import HttpResponse
from django.conf import settings

from core.models import (Customer, DimCustomerUnit, DimReference,
                         SpeedInfringement, Region, Time, Event, Cube, Graphics)
from .serializers import (CustomerSerializer, SpeedInfringementSerializer,
                          DimCustomerUnitSerializer, DimReferenceSerializer,
                          RegionSerializer, TimeSerializer, EventSerializer, CubeSerializer,
                          GraphicsSerializer)
from core.utils import get_db_connection, replace_spaces, replace_underscore


class CustomerList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all customers.

    `POST`: Add a new customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail of a customers.

    `PUT`: Updates customer information.

    `DELETE`: Deletes Customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pk_url_kwarg = 'customer_id'


class DimCustomerUnitList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all customer units.

    `POST`: Add a customer unit.
    """

    queryset = DimCustomerUnit.objects.all()
    serializer_class = DimCustomerUnitSerializer


class DimCustomerUnitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a customer unit.

    `PUT`: Updates a customer unit's information.

    `DELETE`: Deletes a customer unit.
    """

    queryset = DimCustomerUnit.objects.all()
    serializer_class = DimCustomerUnitSerializer
    pk_url_kwarg = 'unit_id'


class DimReferenceList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all references.

    `POST`: Add a reference.
    """

    queryset = DimReference.objects.all()
    serializer_class = DimReferenceSerializer


class DimReferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a reference.

    `PUT`: Updates a reference.

    `DELETE`: Deletes a reference.
    """

    queryset = DimReference.objects.all()
    serializer_class = DimReferenceSerializer
    pk_url_kwarg = 'ref_id'


class SpeedInfringementList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all speed infringements.

    `POST`: Add a speed infringement.
    """

    queryset = SpeedInfringement.objects.all()
    serializer_class = SpeedInfringementSerializer


class SpeedInfringementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a speed infringement.

    `PUT`: Updates speed infringement information.

    `DELETE`: Deletes speed infringement.
    """

    queryset = SpeedInfringement.objects.all()
    serializer_class = SpeedInfringementSerializer
    pk_url_kwarg = 'spinf_id'


class RegionList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all regions.

    `POST`: Add a region.
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a region.

    `PUT`: Updates region information.

    `DELETE`: Deletes region.
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pk_url_kwarg = 'region_id'


class TimeList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all times.

    `POST`: Add a time.
    """

    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a region.

    `PUT`: Updates region information.

    `DELETE`: Deletes region.
    """

    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    pk_url_kwarg = 'time_id'


class EventList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all events.

    `POST`: Add an event.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about an event.

    `PUT`: Updates event information.

    `DELETE`: Deletes event.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pk_url_kwarg = 'event_id'


class CubeList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all cubes.

    `POST`: Add a cube.
    """

    queryset = Cube.objects.all()
    serializer_class = EventSerializer


class CubeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a cube.

    `PUT`: Updates cube information.

    `DELETE`: Deletes a cube.
    """

    queryset = Cube.objects.all()
    serializer_class = EventSerializer
    pk_url_kwarg = 'id'


class GraphicsList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all graphics.

    `POST`: Add a graphics.
    """

    queryset = Graphics.objects.all()
    serializer_class = EventSerializer


class GraphicsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a graphics.

    `PUT`: Updates graphics information.

    `DELETE`: Deletes a graphics.
    """

    queryset = Cube.objects.all()
    serializer_class = EventSerializer
    pk_url_kwarg = 'id'


class MaxYearSpeedInfringementQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by year.
    """

    def get(self, request):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT year(MEC_FECCOMUNDW) as year,' +
                       'count(year(MEC_FECCOMUNDW)) as count FROM ' +
                       'topicosbd.factexcesovelocidad GROUP BY ' +
                       'year(MEC_FECCOMUNDW);')
        years = [{"url": request.build_absolute_uri(reverse("api:max-month-query",
                  kwargs={"year": year[0]})),
                  "label": year[0], "count": year[1]} for year in cursor]
        cursor.close()
        connection.close()
        data = {"data": years}
        return Response(data)


class MaxMonthSpeedInfringementQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by month.
    """

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT month(MEC_FECCOMUNDW) as month," +
                       "count(month(MEC_FECCOMUNDW)) as count FROM " +
                       "topicosbd.factexcesovelocidad WHERE " +
                       "year(MEC_FECCOMUNDW)=%s GROUP BY " +
                       "month(MEC_FECCOMUNDW);", (year,))
        months = [{"url": request.build_absolute_uri(reverse("api:max-day-query",
                   kwargs={"year": year, "month": month[0]})),
                   "label": month[0], "count": month[1]} for month in cursor]
        cursor.close()
        connection.close()
        data = {"data": months}
        return Response(data)


class MaxDaySpeedInfringementQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by day.
    """

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT day(MEC_FECCOMUNDW) as day," +
                       "count(day(MEC_FECCOMUNDW)) as count FROM " +
                       "topicosbd.factexcesovelocidad WHERE " +
                       "year(MEC_FECCOMUNDW)=%s AND month(MEC_FECCOMUNDW)=%s" +
                       " GROUP BY day(MEC_FECCOMUNDW);", (year, month,))
        days = [{"label": day[0], "count": day[1]} for day in cursor]
        cursor.close()
        connection.close()
        data = {"data": days}
        return Response(data)


class MaxFifteenthSpeedInfringementQuery(views.APIView):
    """
    `GET`: Returns a count of infringement for every 15 days.
    """

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT CONCAT(DATE_FORMAT(MEC_FECCOMUNDW, '%%b %%Y Day '), " +
            "case when dayofmonth(MEC_FECCOMUNDW) < 16 then '01-15' " +
            "else CONCAT('16-', right( last_day(MEC_FECCOMUNDW), 2)) " +
            "end) as CharMonth, count(*) as count FROM " +
            "topicosbd.factexcesovelocidad WHERE year(MEC_FECCOMUNDW)=%s " +
            "AND month(MEC_FECCOMUNDW)=%s GROUP BY CharMonth;",
            (year, month,)
        )
        fifteenths = [{"label": fifteenth[0], "count": fifteenth[1]}
                      for fifteenth in cursor]
        cursor.close()
        connection.close()
        data = {"data": fifteenths}
        return Response(data)


class SpeedInfringementByRegionQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by region.
    """

    def get(self, request):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT r.sDpto, count(*) FROM ' +
                       'topicosbd.factexcesovelocidad f INNER JOIN ' +
                       'topicosbd.dimreferenciasdw r ON f.idReferencia = ' +
                       'r.idReferencia GROUP BY r.sDpto;')
        regions = [{"url": request.build_absolute_uri(reverse("api:max-province-query",
                    kwargs={"region": replace_spaces(region[0].lower())})),
                    "label": region[0], "count": region[1]}
                   for region in cursor]
        cursor.close()
        connection.close()
        data = {"data": regions}
        return Response(data)


class SpeedInfringementByProvinceQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by province.
    """

    def get(self, request, *args, **kwargs):
        region = replace_underscore(kwargs.get('region'))
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT r.sProvi, count(*) FROM ' +
                       'topicosbd.factexcesovelocidad f INNER JOIN ' +
                       'topicosbd.dimreferenciasdw r ON f.idReferencia = ' +
                       'r.idReferencia WHERE r.sDpto = %s GROUP BY r.sProvi;',
                       (region,))
        provinces = [{"url": request.build_absolute_uri(reverse("api:max-district-query",
                      kwargs={"region": replace_spaces(region.lower()),
                      "province": replace_spaces(province[0].lower())})),
                     "label": str(province[0]), "count": province[1]}
                     for province in cursor]
        cursor.close()
        connection.close()
        data = {"data": provinces}
        return Response(data)


class SpeedInfringementByDistrictQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by district.
    """

    def get(self, request, *args, **kwargs):
        region = replace_underscore(kwargs.get('region'))
        province = replace_underscore(kwargs.get('province'))
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT r.sDistr, count(*) FROM ' +
                       'topicosbd.factexcesovelocidad f INNER JOIN ' +
                       'topicosbd.dimreferenciasdw r ON f.idReferencia = ' +
                       'r.idReferencia WHERE r.sDpto = %s AND r.sProvi = %s ' +
                       'GROUP BY r.sDistr;',
                       (region, province,))
        districts = [{"url": request.build_absolute_uri(reverse("api:max-road-query",
                      kwargs={"region": replace_spaces(region.lower()),
                      "province": replace_spaces(province.lower()),
                      "district": (replace_spaces(district[0].lower())
                      if district[0] != '' else 'empty')})),
                     "label": district[0], "count": district[1]}
                     for district in cursor]
        cursor.close()
        connection.close()
        data = {"data": districts}
        return Response(data)


class SpeedInfringementByRoadQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by month.
    """

    def get(self, request, *args, **kwargs):
        region = replace_underscore(kwargs.get('region'))
        province = replace_underscore(kwargs.get('province'))
        district = (replace_underscore(kwargs.get('district'))
                    if kwargs.get('district') != 'empty' else '')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT r.sNomVia, count(*) FROM ' +
                       'topicosbd.factexcesovelocidad f INNER JOIN ' +
                       'topicosbd.dimreferenciasdw r ON f.idReferencia = ' +
                       'r.idReferencia WHERE r.sDpto = %s AND r.sProvi = %s ' +
                       'AND r.sDistr = %s GROUP BY r.sNomVia;',
                       (region, province, district))
        roads = [{"label": road[0], "count": road[1]} for road in cursor]

        roads = roads[1:51]
        cursor.close()
        connection.close()
        data = {"data": roads}
        return Response(data)
