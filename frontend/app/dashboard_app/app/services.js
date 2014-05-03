'use strict';

/* Services */

App.services = angular.module('Services', ['ngResource']);

App.services.factory('SpeedInfringementsYear', function($resource) {
    var SpeedInfringementsYear = $resource(App.API + 'speed-infringements/max-year', {});
    return SpeedInfringementsYear;
});


App.services.factory('SpeedInfringementsMonth', function($resource) {
    var SpeedInfringementsMonth = $resource(App.API + 'speed-infringements/max-month/:year', {});
    return SpeedInfringementsMonth;
});


App.services.factory('SpeedInfringementsDay', function($resource) {
    var SpeedInfringementsMonth = $resource(App.API + 'speed-infringements/max-day/:year/:month', {});
    return SpeedInfringementsMonth;
});

App.services.factory('SpeedInfringementsRegion', function($resource) {
    var SpeedInfringementsYear = $resource(App.API + 'speed-infringements/max-region', {});
    return SpeedInfringementsYear;
});


App.services.factory('SpeedInfringementsProvince', function($resource) {
    var SpeedInfringementsMonth = $resource(App.API + 'speed-infringements/max-province/:region', {});
    return SpeedInfringementsMonth;
});


App.services.factory('SpeedInfringementsDistrict', function($resource) {
    var SpeedInfringementsMonth = $resource(App.API + 'speed-infringements/max-district/:region/:province', {});
    return SpeedInfringementsMonth;
});

App.services.factory('SpeedInfringementsRoad', function($resource) {
    var SpeedInfringementsMonth = $resource(App.API + 'speed-infringements/max-road/:region/:province/:district', {});
    return SpeedInfringementsMonth;
});