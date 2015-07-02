/**
 * User: KiRoader
 * Date: 15-7-2
 * Time: 下午9:00
 */
 var app = angular.module("scoreInputApp", ['teacher.requestSvc']);

 app.controller('scoreInputController', function($scope, $window){


 	function _getData() {
                    students.get($window.class_id).success(function (event) {
                        if (event.status == 200) {
                            $scope.items = event.data.students;
                        }
                    })
                }
    _getData();

    $scope.goDetails = function($event, item){
                    $event.preventDefault();
                    $window.location.href = "/teacher/message/" + msg.id + "/";
 });