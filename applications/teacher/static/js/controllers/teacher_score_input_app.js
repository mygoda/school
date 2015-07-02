/**
 * User: KiRoader
 * Date: 15-6-29
 * Time: 下午15:00
 */
 var app = angular.module("scoreInputApp", ['teacher.requestSvc']);

 app.controller('scoreInputController', function($scope, $window){


 	function _getData() {
                    student_grade.get($window.teacher).success(function (event) {
                        if (event.status == 200) {
                            $scope.students = event.data.students;
                        }
                    })
                }
    _getData();

 	
 });