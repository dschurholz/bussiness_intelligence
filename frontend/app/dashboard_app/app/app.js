'use strict';

/* App Module */

var App = { API : 'http://localhost:8000/api/v1/',
            BaseURl : 'http://localhost:8000/',
            scope: null};

App.ng = angular.module('businessintelligence', ['Services', 'ngCookies', 'ngRoute']);

App.ng.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/', { templateUrl: 'views/main.html', controller: MainCtrl }).
      otherwise({redirectTo: '/'});
}]);
