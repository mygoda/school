
var app = angular.module("loginApp", ['teacher.requestSvc']);

app.controller("loginCtrl", ['$scope', 'login', '$window', function($scope, login, $window){
    $scope.loginData = {};

    $scope.sendLoginData = function($event){
        $event.preventDefault();

        _params = {
        phone: $scope.loginData.name,
        password: $scope.loginData.verifypassword,
        };

        login.post(_params).success(function (data, status) {
                        if (status == 200) {
                            $window.location.href = '/teacher/index/';

                           }}).error(function (data) {
                                alert('对不起，用户名或者密码错误，请重新输入');
        });
    }
}])
