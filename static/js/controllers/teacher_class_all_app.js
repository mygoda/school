var app = angular.module("classApp", []);

app.controller('classController', function($scope){

	$scope.clases = [
					{"which": '三年级2班'},
					{"which": '三年级3班'},
					{"which": '三年级5班'},
	];

	
});