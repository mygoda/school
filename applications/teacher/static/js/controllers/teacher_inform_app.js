var app = angular.module("informApp", ['teacher.requestSvc']);

app.controller('informController', [function($scope, $window){

//	$scope.messages = [
//					{"where": '学校', "time": '6月30号', "message": '明天下午三点理工一129开会'},
//					{"where": '家长', "time": '6月27号', "message": '明天下午三点理工一129开会'},
//					{"where": '学校', "time": '6月24号', "message": '明天下午三点理工一129开会'},
//					{"where": '家长', "time": '6月21号', "message": '明天下午三点理工一129开会'},
//	];

    function _getData() {
                    message.get($window.teacher).success(function (event) {
                        if (event.status == 200) {
                            $scope.messages = event.data.teacherMessages;
                        }
                    })
                }
    _getData();

	$scope.goDetails = function($event, msg){
                    $event.preventDefault();
                    $window.location.href = "/teacher/message/" + msg.id + "/";
                };
	
});