var jetBov = angular.module('jetBov', [
    'ngResource',
])

.config(function($httpProvider, $resourceProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    // $httpProvider.defaults.withCredentials = true;
    $resourceProvider.defaults.stripTrailingSlashes = false;
})