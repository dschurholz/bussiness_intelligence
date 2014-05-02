from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status

from django.db.models import Count
from django.http import HttpResponse
from django.conf import settings

from core.models import (Customer, DimCustomerUnit, DimReference,
                         SpeedInfringement, Region, Time, Event)

from .serializers import (CustomerSerializer, SpeedInfringementSerializer,
                          DimCustomerUnitSerializer, DimReferenceSerializer,
                          RegionSerializer, TimeSerializer, EventSerializer)
from core.utils import get_db_connection


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
        years = [{"label": year[0], "count": year[1]} for year in cursor]
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
        months = [{"label": month[0], "count": month[1]} for month in cursor]
        cursor.close()
        connection.close()
        data = {"data": months}
        return Response(data)


class MaxDaySpeedInfringementQuery(views.APIView):
    """
    `GET`: Returns a count of infringement by month.
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
    `GET`: Returns a count of infringement by month.
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
