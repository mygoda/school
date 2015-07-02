var app = angular.module("examApp", []);

app.controller('examController', function($scope){

	$scope.subjects = [
					{"subject": '计算机', "name": '第一次模拟考试', "time": '2015-9-8'},
					{"subject": '计算机', "name": '第二次模拟考试', "time": '2015-10-8'},
					{"subject": '计算机', "name": '期中考试', "time": '2015-11-8'},
					{"subject": '计算机', "name": '期末考试', "time": '2015-12-8'},
		];

	
});