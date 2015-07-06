var app = angular.module("scoreApp", ['teacher.requestSvc']);

app.controller("scoreController", ['$scope', 'grades', function($scope, grades){


	function _getData() {
                    grades.get(window.term).success(function(data, status) {
                        if (status == 200) {
                            $scope.students = data.data.students_grade;
                        }
                    })
                }
    _getData();
}])