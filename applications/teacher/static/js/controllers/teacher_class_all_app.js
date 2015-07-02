
var app = angular.module("classApp", []);

app.controller('classController', function($scope){

	function _getData() {
                    classes.get($window.teacher).success(function (event) {
                        if (event.status == 200) {
                            $scope.classes = event.data.teacher_classes;
                        }
                    })
                }
    _getData();

    $scope.goDetails = function($event, class){
                    $event.preventDefault();
                    $window.location.href = "teacher/class/" + class.id +"/detail/";
});