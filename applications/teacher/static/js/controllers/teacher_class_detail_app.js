/**
 * User: wangxiaottt
 * Date: 15-4-15
 * Time: 下午3:23
 */
(function (angular, win) {
    win.App = angular.module('meetingApp', [
            'ngTouch'
            , 'ngRoute'
            , 'filterDirc'
            , 'tabDirc'
            , 'meeting.requestSvc'
            , 'meeting.userSvc'
        ])

        .constant('root', '/static/template/')

        .config(["$routeProvider", "$locationProvider", "root",
            function ($routeProvider, $locationProvider, root) {
                $routeProvider
                    //会员卡设置
                    .when("/students", {templateUrl: root + "class_students_tpl.html", controller: "infoCtrl"})
                    .when("/terms", {templateUrl: root + "class_term_tpl.html", controller: "schedulesCtrl"})
                    .when("/tickets", {templateUrl: root + "terms_tpl.html", controller: "ticketsCtrl"})
                    .when("/login", {templateUrl: root + "teacher_login_tpl.html", controller: "loginCtrl"})
                    .otherwise({redirectTo: "/terms"});
            }])

        .controller('meetingCtrl', ['$scope', '$location', 'userSvc',
            function ($scope, $location, userSvc) {
                var _path = $location.path(),
                    _tabConfig = {},
                    _pathLst = ['/info', '/schedules', '/tickets'];

                switch (_path) {
                    case '/info':
                        _tabConfig.index = 0;
                        break;
                    case "/schedules":
                        _tabConfig.index = 1;
                        break;
                    case "/tickets":
                        _tabConfig.index = 2;
                        break;
                    case "/login":
                        _tabConfig.index = 2;
                        break;
                    default :
                        _tabConfig.index = 0;
                }


                _tabConfig.tabLst = [
                    {name: '基本信息'},
                    {name: '日程安排'},
                    {name: '我的门票'}
                ];

                _tabConfig.onTabChangeCb = function (index) {
                    if ((index) == 2 && !userSvc.isLogin) {
                        $location.path('/login');
                        return;
                    }
                    if ($location.path() != _pathLst[index])
                        $location.path(_pathLst[index])
                };

                $scope.tabConfig = _tabConfig;
            }])

        .controller('infoCtrl', ['$scope', '$sce', 'getMeeting', 'meeting', '$window', 'userSvc',
            function ($scope, $sce, getMeeting, meeting, $window, userSvc) {
                var _id = getMeeting.id;

                function _getData() {
                    meeting.get(_id).success(function (event) {
                        if (event.status == 200) {
                            $scope.meeting = event.data.meeting;
                            $scope.meeting.description = $sce.trustAsHtml(event.data.meeting.description);
                        }
                    })
                }

                $scope.goBuyTicket = function($event){
                    $event.preventDefault();

//                    if(userSvc.isLogin)
                        $window.location.href = '/meetings/' + _id + '/buy/tickets/';
//                    else
//                        $window.location.href = '/users/register/';
                };

                _getData();
            }])

        .controller('schedulesCtrl', ['$scope', '$filter', 'getMeeting', 'schedules', 'userSvc', '$window',
            function ($scope, $filter, getMeeting, schedules, userSvc, $window) {
                this.firstTime = true;
                var _self = this,
                    _id = getMeeting.id;


                $scope.goBuyTicket = function ($event) {
                    $event.preventDefault();

//                    if (userSvc.isLogin)
                        $window.location.href = '/meetings/' + _id + '/buy/tickets/';
//                    else
//                        $window.location.href = '/users/register/';
                };

                $scope.goDetails = function($event, item){
                    $event.preventDefault();
                    $window.location.href = "/meetings/schedules/" + item.id + "/";
                };

                function _getData(params) {
                    var _params = {
                        meeting_id: _id,
                        show_all: 1
                    };

                    angular.extend(_params, params);

                    schedules.get(_params).success(function (event) {
                        if (event.status == 200) {
                            var _data = event.data.schedules;
                            var _result = [], _index = 0;

                            angular.forEach(_data, function (value, key) {
                                if (!_result[_index]) {
                                    _result.push({
                                        date: $filter('date')(value.start, 'yyyy-MM-dd'),
                                        data: [value]
                                    })
                                } else {
                                    if ($filter('date')(value.start, 'yyyy-MM-dd') == _result[_index].date) {
                                        _result[_index].data.push(value);
                                    } else {
                                        _index++;
                                        _result.push({
                                            date: $filter('date')(value.start, 'yyyy-MM-dd'),
                                            data: [value]
                                        })
                                    }
                                }
                            });

                            $scope.schedules = _result;
                        }
                    })
                }

                $scope.filterConfig = {
                    url: '/api/schedules/filter/?meeting_id=' + _id,
                    onFilterChange: function (filterData) {
                        if (_self.firstTime) {
                            _self.firstTime = !1;
                            return;
                        }

                        _getData(filterData);
                    }
                };

                _getData();
            }])

        .controller('ticketsCtrl', ['$scope', '$window', '$location', 'userTrade', 'userSvc', 'getMeeting', 'trades',
            function ($scope, $window, $location, userTrade, userSvc, getMeeting, trades) {
                $scope.loaded = !1;
                if (!userSvc.isLogin) {
                    $location.path('/login')
                }
                //去付款
                $scope.goPay = function ($event, item) {
                    $event.preventDefault();
                    $window.location.href = '/meetings/trades/' + item.id + '/';
                };

                $scope.cancelTrade = function($event, item){
                    $event.preventDefault();
                    if(!confirm('确认取消该订单？'))
                        return;
                    trades.delete(item.id).success(function(event){
                        if(event.status == 200){
                            _getData();
                        }else{
                            alert(event.msg?event.msg:'取消订单失败，请重试。');
                        }
                    })
                };

                $scope.logout = function($event){
                    $event.preventDefault();

                    if(!confirm('确认退出登录？')){
                        return;
                    }

                    $window.location.href = '/users/logout/'
                }

                //无票去购票
                $scope.goBuyTickets = function ($event) {
                    $event.preventDefault();
                    $window.location.href = '/meetings/' + getMeeting.id + '/buy/tickets/'
                };

                $scope.goDetails = function ($event, item) {
                    $event.preventDefault();
                    $window.location.href = '/meetings/tickets/' + item.id + '/';
                };

                //修改参会人
                $scope.editAttendee = function($event, item){
                    $event.preventDefault();
                    $window.location.href = '/meetings/tickets/' + item.id + '/modify';
                };

                //去预约课程
                $scope.goOrder = function($event, item){
                    $event.preventDefault();
                    $window.location.href = '/meetings/tickets/' + item.id + '/schedules/';
                };

                function _getData() {
                    userTrade.get({meeting_id:getMeeting.id,show_all:1}).success(function (event) {
                        if (event.status == 200) {
                            $scope.loaded = !0;
                            $scope.trades = event.data.trades;
                        }
                    })
                }

                _getData();
            }])


        .controller('loginCtrl', ['$scope', '$window', '$location', 'userSvc', 'getMeeting',
            function ($scope, $window, $location, userSvc, getMeeting) {
                if(userSvc.isLogin)
                    $location.path('/tickets');

                $scope.goLogin = function ($event) {
                    $event.preventDefault();

                    $window.location.href = '/users/login/?next=' + encodeURIComponent('/meetings/' + getMeeting.id + '/#/tickets');
                }
            }])

        .factory('getMeeting', ['$window', function ($window) {
            var _re = new RegExp("^/meetings/(\\d*)/");
            var _id = $window.location.pathname.match(_re)[1];

            return {
                id: _id
            }
        }])


}(angular, window));
