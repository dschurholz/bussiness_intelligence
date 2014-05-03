'use strict';

/* Controllers */
function MainCtrl($scope, SpeedInfringementsYear, SpeedInfringementsMonth, SpeedInfringementsDay) {
    var builderOfSerie = function(name, data) {
        var serie = { name : name,
                      colorByPoint : true,
                      data : [] };
        for (var i = 0; i < data.length; i++) {
            serie.data.push({ name : data[i].label, y : data[i].count, drilldown : true });
        }
        return serie;
    }

    
    var speedInfsYear = SpeedInfringementsYear.get({}, function() {
        var serie = builderOfSerie("Year", speedInfsYear.data);
        $('#speedInf').highcharts({
            chart: {
                type: 'column',
                events: {
                    drilldown: function (e) {
                        var lchar = $("#speedInf").highcharts();
                        if (e.point.series.name == 'Year') {
                            console.log('Process drilldown year...', e.point.name);
                            var speedInfsMonth = SpeedInfringementsMonth.get({ year : e.point.name }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("Month", speedInfsMonth.data));
                            });
                            return;
                        }
                        if (e.point.series.name == 'Month') {
                            console.log('Process drilldown month...', e.point.name);
                            var cYear = e.currentTarget.drilldownLevels[0].pointOptions.name;
                            var speedInfsDay = SpeedInfringementsDay.get({ year: cYear , month : e.point.name }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("Day", speedInfsDay.data));
                            });
                            return;
                        }
                        if (e.point.series.name == 'Day') {
                            var cYear = e.currentTarget.drilldownLevels[0].pointOptions.name;
                            var cMonth = e.currentTarget.drilldownLevels[1].pointOptions.name;
                            console.log('Process drilldown day...', cYear, cMonth, e.point.name);
                            return;
                        }
                    }
                }
            },
            title: { text: 'Infracciones de velocidad por tiempo' },
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
                type: 'pie',
                events: {
                    drilldown: function (e) {
                        var lchar = $("#speedInfReg").highcharts();
                        if (e.point.series.name == 'Region') {
                            console.log('Process drilldown year...', e.point.name);
                            var speedInfsMonth = SpeedInfringementsProvince.get({ region : e.point.name }, function() {
                                lchar.addSeriesAsDrilldown(e.point, builderOfSerie("Province", speedInfsMonth.data));
                            });
                            return;
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