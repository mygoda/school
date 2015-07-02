/**
 * User: KiRoader
 * Date: 15-6-29
 * Time: 下午15:00
 */
 var app = angular.module("scoreInputApp", []);

 app.controller('scoreInputController', function($scope){

 	$scope.names = [
 				{"name": '小明', "score": '90'},
 				{"name": '小花', "score": '80'},
 				{"name": 'KiRoader', "score": '97'},
 				{"name": 'igoda', "score": '60'},
 				{"name": '小明', "score": '55'},
 				{"name": '小明', "score": '77'},
 				{"name": '小明', "score": '70'}
 			];

 	
 });