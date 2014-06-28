'use strict';

/* Controllers */
function MainCtrl($scope, $http, $cookies, $compile, GraphicList, utilsService) {
    App.scope = $scope;
    $scope.graphics = [];
    $scope.graphicCount = 0;
    GraphicList.get({}, function (data) {
        $scope.graphics = data.results;
        $scope.graphicCount = data.count;
        $scope.buildGraphics();
    });

    $scope.buildGraphics = function () {
        for (var graphic in $scope.graphics) {
            $scope.graphics[graphic].loaded = false;
            var endpoint = $scope.graphics[graphic].query_endpoint + "?query=" +
                           $scope.graphics[graphic].query;
            $http.get(endpoint).success(function (data) {
                //console.log(data);
                var idx = utilsService.searchByProperty(
                    $scope.graphics,
                    'id',
                    data.graphic_id
                );
                $scope.graphics[idx].next = data.next;
                $scope.graphics[idx].previous = data.previous;
                $scope.graphics[idx].loaded = true;
                var serie = builderOfSerie($scope.graphics[idx].name, data.results);
                $('#speedInf-'+$scope.graphics[idx].id).highcharts({
                    chart: {
                        type: $scope.graphics[idx].ds_type,
                    },
                    title: { text: $scope.graphics[idx].name },
                    xAxis: { type: 'category' },
                    legend: { enabled: false },
                    plotOptions: {
                        series: {
                            borderWidth: 0,
                            dataLabels: {
                                enabled: true,
                            }
                        }
                    },
                    series: [serie],
                    drilldown: { series : [] },
                    tooltip: {
                        useHTML: true,
                        formatter: function() {
                            var text = '<span style="font-size: 12px">Infracciones: ' + this.y + '</span><br/>';
                            for (var dim in $scope.graphics[idx].dimentions) {
                                text += '<b style="font-size: 14px">' +
                                        $scope.graphics[idx].dimentions[dim].name +'</b><br/>';
                                for (var hier in $scope.graphics[idx].dimentions[dim].hierarchies) {
                                    var h = utilsService.format('App.scope.graphics[{0}].dimentions[{1}].hierarchies[{2}]',
                                                                  {0:idx, 1:dim, 2:hier}),
                                    n = this.point.name;
                                    text += '&nbsp&nbsp<a style="cursor: pointer;" ' +
                                            'onClick="javascript:App.scope.drilldown(' + h + ',\'' + n + '\', \'' + idx + '\')">' +
                                             $scope.graphics[idx].dimentions[dim].hierarchies[hier].name +'</a><br/>';
                                }
                            }
                            return text;
                        }
                    },
                });
            });
        }
        charts();
    };

    $scope.nextPage = function (graphic) {
        graphic.loaded = false;
        $http.get(graphic.next).success(function (data) {
            console.log(data);
            var idx = utilsService.searchByProperty(
                $scope.graphics,
                'id',
                data.graphic_id
            );
            $scope.graphics[idx].loaded = true;
            $scope.graphics[idx].next = data.next;
            $scope.graphics[idx].previous = data.previous;
            var serie = builderOfSerie($scope.graphics[idx].name, data.results);
            $('#speedInf-'+$scope.graphics[idx].id).highcharts({
                    chart: {
                        type: $scope.graphics[idx].ds_type,
                    },
                    title: { text: $scope.graphics[idx].name },
                    xAxis: { type: 'category' },
                    legend: { enabled: false },
                    plotOptions: {
                        series: {
                            borderWidth: 0,
                            dataLabels: {
                                enabled: true,
                            }
                        }
                    },
                    series: [serie],
                    drilldown: { series : [] },
                    tooltip: {
                        useHTML: true,
                        formatter: function() {
                            var text = '<span style="font-size: 12px">Infracciones: ' + this.y + '</span><br/>';
                            for (var dim in $scope.graphics[idx].dimentions) {
                                text += '<b style="font-size: 14px">' +
                                        $scope.graphics[idx].dimentions[dim].name +'</b><br/>';
                                for (var hier in $scope.graphics[idx].dimentions[dim].hierarchies) {
                                    var h = utilsService.format('App.scope.graphics[{0}].dimentions[{1}].hierarchies[{2}]',
                                                                  {0:idx, 1:dim, 2:hier}),
                                    n = this.point.name;
                                    text += '&nbsp&nbsp<a style="cursor: pointer;" ' +
                                            'onClick="javascript:App.scope.drilldown(' + h + ',\'' + n + '\', \'' + idx + '\')">' +
                                             $scope.graphics[idx].dimentions[dim].hierarchies[hier].name +'</a><br/>';
                                }
                            }
                            return text;
                        }
                    },
                });
        });
    };

    $scope.deleteGraphic = function (graphic) {
        var idx = utilsService.searchByProperty(
            $scope.graphics,
            'id',
            graphic.id
        );
        $scope.graphics.splice(idx, 1);
        $scope.graphicCount--;
        $http({
            method: 'DELETE',
            url: graphic.url,
            headers: {
                'X-CSRFToken': $cookies.csrftoken
            }
        });
    };

    $scope.drilldown = function (hierarchy, pointName, graphicId) {
        console.log(hierarchy);
        console.log(pointName);
        console.log(graphicId);
    };

    var builderOfSerie = function (name, data) {
        var serie = { name : name,
                      colorByPoint : true,
                      data : [] };
        for (var i = 0; i < data.length; i++) {
            serie.data.push({ name : data[i].label, y : data[i].count, z : data[i].count, drilldown : true });
        }
        return serie;
    };

    $scope.$on('graphic_created', function (e, data) {
        console.log(e);
        console.log(data);
        $scope.graphics.push(data.data);
        $scope.graphicCount++;
        $scope.buildGraphics();
    });
}

function RegionCtrl($scope, SpeedInfringementsRegion, SpeedInfringementsProvince, SpeedInfringementsDistrict, SpeedInfringementsRoad) {
    var builderOfSerie = function(name, data) {
        var serie = { name : name,
                      colorByPoint : true,
                      data : [] };
        for (var i = 0; i < data.length; i++) {
            serie.data.push({ name : data[i].label, y : data[i].count, drilldown : true });
        }
        return serie;
    }

    
    var speedInfsRegion = SpeedInfringementsRegion.get({}, function() {
        var serie = builderOfSerie("Region", speedInfsRegion.data);
        $('#speedInfReg').highcharts({
            chart: {
                type: 'column',
                events: {
                    drilldown: function (e) {
                        var lchar = $("#speedInfReg").highcharts();
                        if (e.point.series.name == 'Region') {
                            console.log('Process drilldown year...', e.point.name);
                            var speedInfsMonth = SpeedInfringementsProvince.get({ region : e.point.name }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("Province", speedInfsMonth.data));
                            });
                            returncolumn
                        }
                        if (e.point.series.name == 'Province') {
                            console.log('Process drilldown month...', e.point.name);
                            var cYear = e.currentTarget.drilldownLevels[0].pointOptions.name;
                            var speedInfsDay = SpeedInfringementsDistrict.get({ region: cYear , province : e.point.name }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("District", speedInfsDay.data));
                            });
                            return;
                        }
                        if (e.point.series.name == 'District') {
                            var cYear = e.currentTarget.drilldownLevels[0].pointOptions.name;
                            var cMonth = e.currentTarget.drilldownLevels[1].pointOptions.name;
                            console.log('Process drilldown day...', cYear, cMonth, e.point.name);
                            var speedInfsDay = SpeedInfringementsRoad.get({ region: cYear , province : cMonth, district: e.point.name.replace(" ","_") }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("Road", speedInfsDay.data));
                            });
                            return;
                        }
                        if (e.point.series.name == 'Road') {
                            var cYear = e.currentTarget.drilldownLevels[0].pointOptions.name;
                            var cMonth = e.currentTarget.drilldownLevels[1].pointOptions.name;
                            var cDistr = e.currentTarget.drilldownLevels[2].pointOptions.name;
                            console.log('Process drilldown day...', cYear, cMonth, cDistr, e.point.name);
                            return;
                        }
                    }
                }
            },
            title: { text: 'Infracciones de velocidad por Region' },
            xAxis: { type: 'category' },
            legend: { enabled: false },
            plotOptions: {
                series: {
                    borderWidth: 0,
                    dataLabels: {
                        enabled: true,
                    }
                }
            },
            series: [serie],
            drilldown: { series : [] },
        });

    });

    // Build chars example cubo 1 cubo 2
    charts();

}