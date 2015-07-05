
var app = angular.module("classApp", ['teacher.requestSvc']);

app.controller('classController', ['$scope', 'classes', function($scope, classes){

	function _getData() {
                    classes.get(window.teacher).success(function (data, status) {
                        if (status == 200) {
                            $scope.classes = data.data.teacher_classes;
                        }
                    })
                }
    _getData();

    $scope.goDetails = function($event, name){
                    $event.preventDefault();
                    $window.location.href = "/teacher/class/" + name.id +"/detail/";
}
}]);