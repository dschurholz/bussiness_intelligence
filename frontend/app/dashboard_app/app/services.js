'use strict';

/* Services */

App.services = angular.module('Services', ['ngResource']);

App.services.factory('SpeedInfringementsYear', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-year', {});
    return res;
});


App.services.factory('SpeedInfringementsMonth', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-month/:year', {});
    return res;
});


App.services.factory('SpeedInfringementsDay', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-day/:year/:month', {});
    return res;
});

App.services.factory('SpeedInfringementsRegion', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-region', {});
    return res;
});


App.services.factory('SpeedInfringementsProvince', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-province/:region', {});
    return res;
});


App.services.factory('SpeedInfringementsDistrict', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-district/:region/:province', {});
    return res;
});

App.services.factory('SpeedInfringementsRoad', function($resource) {
    var res = $resource(App.API + 'speed-infringements/max-road/:region/:province/:district', {});
    return res;
});

App.services.factory('DimentionList', function($resource) {
    var res = $resource(App.API + 'dimentions', {});
    return res;
});

App.services.factory('DimentionDistinctList', function($resource) {
    var res = $resource(App.API + 'dimentions?distinct=True', {});
    return res;
});

App.services.factory('Dimention', function($resource) {
    var res = $resource(App.API + 'dimentions/:dimention', {});
    return res;
});

App.services.factory('HierarchyList', function($resource) {
    var res = $resource(App.API + 'hierarchies', {});
    return res;
});

App.services.factory('HierarchyDistinctList', function($resource) {
    var res = $resource(App.API + 'hierarchies?dimention=:dimention&distinct=True', {});
    return res;
});

App.services.factory('Hierarchy', function($resource) {
    var res = $resource(App.API + 'hierarchies/:hierarchy', {});
    return res;
});

App.services.factory('GraphicList', function($resource) {
    var res = $resource(App.API + 'graphics', {});
    return res;
});

App.services.service('utilsService', [
        function () {
            this.searchByProperty = function (array, propertyName, propertyValue) {
                var idx, found = false;
                for (idx in array) {
                    if (array[idx][propertyName] === propertyValue) {
                        found = true;
                        return idx;
                    }
                }
                if (!found) {
                    return -1;
                }
            };

            this.format = function (string, formatObj) {
                return string.replace(/{(\d+)}/g, function (match, number) {
                    return typeof formatObj[number] != 'undefined'
                        ? formatObj[number]
                        : match;
                });
            };
        }
]);