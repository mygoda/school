/**
 * User: KiRoader
 * Date: 15-6-29
 * Time: 下午15:00
 */
 var app = angular.module("scoreInputApp", ['teacher.requestSvc']);

 app.controller('scoreInputController', ['$scope', '$window', 'student_grade', function($scope, $window, student_grade){


 	function _getData() {
                    student_grade.get(window.school_class).success(function(data, status) {
                        if (status == 200) {
                            $scope.students = data.data.students;
                        }
                    })
                }
    _getData();

    _params = {
        term: window.term,
        data: $scope.students
    }

    student_grade.post(_params).success(function (data, status) {
                        if (status == 200) {
                            var term = data.data.term;
                            $window.location.href = '/teacher/record/grade/success/?term' + term;
                        }
                    })

 	
 }]);