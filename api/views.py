from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status

from django.conf import settings

from core.models import (Customer, DimCustomerUnit, DimReference,
                         SpeedInfringement, Region, Time, Event, Cube,
                         Graphics, Dimention, Hierarchy)
from .serializers import (CustomerSerializer, SpeedInfringementSerializer,
                          DimCustomerUnitSerializer, DimReferenceSerializer,
                          RegionSerializer, TimeSerializer, EventSerializer,
                          CubeSerializer, GraphicsSerializer,
                          DimentionSerializer, HierarchySerializer,
                          SimpleDimentionSerializer, SimpleHierarchySerializer,
                          SQLQuerySerializer)
from core.utils import (get_db_connection, replace_spaces, replace_underscore,
                        get_hier_order)
from constants import ON_QUERY, DIM_SCUT


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
    serializer_class = CubeSerializer


class CubeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a cube.

    `PUT`: Updates cube information.

    `DELETE`: Deletes a cube.
    """

    queryset = Cube.objects.all()
    serializer_class = CubeSerializer
    pk_url_kwarg = 'id'


class DimentionList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all dimentions.

    `POST`: Add a dimention.
    """

    queryset = Dimention.objects.all()
    serializer_class = DimentionSerializer

    def filter_queryset(self, queryset):
        distinct = self.request.QUERY_PARAMS.get('distinct')
        if distinct:
            queryset = queryset.values('name', 'table_name').distinct()
            self.serializer_class = SimpleDimentionSerializer
        return queryset


class DimentionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a dimention.

    `PUT`: Updates dimention information.

    `DELETE`: Deletes a dimention.
    """

    queryset = Cube.objects.all()
    serializer_class = DimentionSerializer
    pk_url_kwarg = 'id'


class HierarchyList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all hierarchies.

    `POST`: Add a hierarchy.
    """

    queryset = Hierarchy.objects.all()
    serializer_class = HierarchySerializer
    dimention = None

    def filter_queryset(self, queryset):
        distinct = self.request.QUERY_PARAMS.get('distinct')
        dimention = self.request.QUERY_PARAMS.get('dimention')
        if dimention:
            queryset = queryset.filter(dimention__name=dimention)
            self.dimention = dimention
        if distinct:
            queryset = queryset.values('name', 'columne_name').distinct()
            self.serializer_class = SimpleHierarchySerializer
        return queryset

    def list(self, request, *args, **kwargs):
        response = super(HierarchyList, self).list(request, args, kwargs)
        if self.dimention:
            response.data['dimention'] = self.dimention
        return response


class HierarchyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a hierarchy.

    `PUT`: Updates hierarchy information.

    `DELETE`: Deletes a hierarchy.
    """

    queryset = Hierarchy.objects.all()
    serializer_class = HierarchySerializer
    pk_url_kwarg = 'id'


class CreateGraphic(views.APIView):
    """
    `POST`: Creates a new graphic, including, cube, dimentions and hierarchies.
    """

    def post(self, request, *args, **kwargs):
        #import json
        #print json.dumps(request.DATA)
        data = request.DATA
        response = {}
        if data["hierarchies"]:
            query = ("SELECT %s, count(*) as count " +
                     "FROM topicosbd.factexcesovelocidad f " +
                     "INNER JOIN %s " +
                     "GROUP BY %s;")
            dimentions_query = []
            hierarchies_query = []
            on_query = []
            cube = Cube.create_new_cube(name=data["name"])
            for dim in data["hierarchies"]:
                dimention = Dimention.create_new_dimention(
                    name=dim["dimention_name"],
                    table_name=dim["dimention_table"],
                    cube=cube
                )
                dimentions_query.append("topicosbd." + dim["dimention_table"] +
                                        " " + DIM_SCUT[dim["dimention_table"]] +
                                        " " + ON_QUERY[dim["dimention_table"]])
                for hier in dim["hierarchies"]:
                    hierarchy = Hierarchy.create_new_hierarchy(
                        name=hier["name"],
                        columne_name=hier["columne_name"],
                        dimention=dimention
                    )
                    hierarchies_query.append(hier["columne_name"])

            selected_hier = get_hier_order(hierarchies_query)[0]
            query = query % (
                selected_hier,
                " INNER JOIN ".join(dimentions_query),
                selected_hier
            )
            print query
            try:
                graphic = Graphics.create_new_graphic(
                    name=data["name"],
                    ds_type=data["type"],
                    cube=cube,
                    query=query
                )
            except ConnectionErr:
                response = {"error": "Name exists!"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            response = GraphicsSerializer(graphic).data
            return Response(response)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class GraphicQuery(generics.ListAPIView):
    """
    `GET`: Returns the execution of a SQL query given in a param.
    """

    serializer_class = SQLQuerySerializer

    def get_queryset(self):
        query = self.request.QUERY_PARAMS.get('query')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        records = [{"label": record[0], "count": record[1]}
                   for record in cursor]
        cursor.close()
        connection.close()
        return records

    def list(self, request, *args, **kwargs):
        id = kwargs.get('id')
        response = super(GraphicQuery, self).list(request, args, kwargs)
        response.data['graphic_id'] = int(id)
        return response


class GraphicDrilldown(views.APIView):
    """
    `GET`: Returns the drilldown query given some parameters.
    """

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        hierarchy = self.request.QUERY_PARAMS.get('hierarchy')
        point = self.request.QUERY_PARAMS.get('point')
        graphic = Graphics.objects.get(pk=id)
        


class GraphicsList(generics.ListAPIView):
    """
    `GET`: Returns a list of all graphics.
    """

    queryset = Graphics.objects.all()
    serializer_class = GraphicsSerializer


class GraphicsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a graphics.

    `PUT`: Updates graphics information.

    `DELETE`: Deletes a graphics.
    """

    queryset = Graphics.objects.all()
    serializer_class = GraphicsSerializer
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
        years = [{"url": request.build_absolute_uri(reverse(
                  "api:max-month-query",
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
        months = [{"url": request.build_absolute_uri(reverse(
                   "api:max-day-query",
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
        regions = [{"url": request.build_absolute_uri(reverse(
                    "api:max-province-query",
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
        provinces = [{"url": request.build_absolute_uri(reverse(
                      "api:max-district-query",
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
        districts = [{"url": request.build_absolute_uri(reverse(
                      "api:max-road-query",
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
