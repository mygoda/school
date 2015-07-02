var app = angular.module("informApp", []);

app.controller('informController', function($scope){

	$scope.messages = [
					{"where": '学校', "time": '6月30号', "message": '明天下午三点理工一129开会'},
					{"where": '家长', "time": '6月27号', "message": '明天下午三点理工一129开会'},
					{"where": '学校', "time": '6月24号', "message": '明天下午三点理工一129开会'},
					{"where": '家长', "time": '6月21号', "message": '明天下午三点理工一129开会'},
	];
	
});