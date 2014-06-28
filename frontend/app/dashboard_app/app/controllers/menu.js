'use strict';

function MenuCtrl($scope, $http, $cookies,
                  DimentionDistinctList, HierarchyDistinctList, utilsService) {
    $scope.selectedHierarchies = [];
    $scope.newGraphicName = "";

	DimentionDistinctList.get({}, function(dimentions) {
        $scope.dimentions = dimentions.results;
        for (var dim in $scope.dimentions) {
            $scope.selectedHierarchies.push({
                dimention_name: $scope.dimentions[dim].name,
                dimention_table: $scope.dimentions[dim].table_name,
                hierarchies: []}
            );
        	HierarchyDistinctList.get({dimention: $scope.dimentions[dim].name}, function(hierarchies) {
                var idx = utilsService.searchByProperty(
        			$scope.dimentions,
        			'name',
        			hierarchies.dimention
        		);
        		$scope.dimentions[idx].hierarchies = hierarchies.results;
                for (var hierarchy in $scope.dimentions[idx].hierarchies) {
                    $scope.dimentions[idx].hierarchies[hierarchy].check = false;
                }
        	});
        }
    });

    $scope.chartTypes = [{name: "Area", type:"area"},
                         {name: "Area Range", type:"arearange"},
                         {name: "Area Spline", type:"areaspline"},
                         {name: "Area Spline Range", type:"areasplinerange"},
                         {name: "Bar", type:"bar"},
                         {name: "Boxplot", type:"boxplot"},
                         {name: "Bubble", type:"bubble"},
                         {name: "Column", type:"column"},
                         {name: "Column Range", type:"columnrange"},
                         {name: "Error Bar", type:"errorbar"},
                         {name: "Gauge", type:"gauge"},
                         {name: "Heatmap", type:"heatmap"},
                         {name: "Line", type:"line"},
                         {name: "Pie", type:"pie"},
                         {name: "Pyramid", type:"pyramid"},
                         {name: "Series", type:"series"},
                         {name: "Splines", type:"spline"},
                         {name: "Waterfall", type:"waterfall"}];
    $scope.selectedType = $scope.chartTypes[7];

    $scope.createGraphic = function() {
        //console.log($scope.newGraphicName);
        //console.log($scope.selectedType);
        //console.log($scope.selectedHierarchies);
        if (hierarchiesListIsEmpty()) {
            alert("Seleccione al menos una jerarquía!");
        } else if (!$scope.newGraphicName) {
            alert("Ingrese un nombre para el gráfico!");
        } else {
            var finalHierarchies = [];
            for (var dim in $scope.selectedHierarchies) {
              if ($scope.selectedHierarchies[dim].hierarchies.length > 0) {
                finalHierarchies.push($scope.selectedHierarchies[dim]);
              }
            }
            var graphic = {
                name: $scope.newGraphicName,
                type: $scope.selectedType.type,
                hierarchies: finalHierarchies
            };
            $http({
                method: 'POST',
                url: App.API + 'graphics/create',
                data: graphic,
                headers: {'X-CSRFToken': $cookies.csrftoken},
            }).success(function (data, status) {
                console.log(data);
                $scope.$parent.$broadcast('graphic_created', {
                    data: data
                });
            });
        }
    };

    $scope.checkHierarchy = function (hierarchy, dimention) {
        var idx = utilsService.searchByProperty(
            $scope.selectedHierarchies,
            'dimention_name',
            dimention.name
        );
        var idx2 = $scope.selectedHierarchies[idx].hierarchies.indexOf(hierarchy);
        if (idx2 != -1) {
            $scope.selectedHierarchies[idx].hierarchies.splice(idx2, 1);
        } else {
            $scope.selectedHierarchies[idx].hierarchies.push(hierarchy);
        }
    };

    function hierarchiesListIsEmpty () {
        for (var h in $scope.selectedHierarchies) {
            if ($scope.selectedHierarchies[h].hierarchies.length > 0) {
                return false;
            }
        }
        return true;
    };
};