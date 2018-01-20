jetBov
.controller('jetbovController', function ($scope, gadoService) {
    var self = this;
    self.pesagens = [];
    
    console.log('Gado')
    gadoService.query({expand:'fazenda'}).then(function(response){
        console.log(self.pesagens)
        self.pesagens = response.results;
        $scope.pesagens = response.results;
        console.log(self.pesagens)
    }, function(err){
        concole.log('err')
    })

})
    