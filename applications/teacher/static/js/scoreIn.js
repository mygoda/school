var scoreApp = angular.module("scoreApp", []);

scoreApp.controller = ('scoreContr', function($scope){
	$scope.scores = [
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'},
				{"name": '小明', "score": '89'}
	];

});