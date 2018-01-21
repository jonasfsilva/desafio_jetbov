jetBov
.controller('jetbovController', function ($scope, gadoService, pesagemService) {
    var self = this;
    self.pesagens = [];
    self.fazenda_cnpj = null;
    self.token = null;
    self.numero_brinco = null;
    self.show_list = false;

    self.pesquisar_por_cnpj = function(){
        $scope.pesagens = [];
        self.show_list = false;
        pesagemService.query({gado__fazenda__cnpj: self.fazenda_cnpj, expand:'gado'}).then(function(response){
            $scope.pesagens = response.results;
            self.show_list = true;
        }, function(err){
            console.log('err')
        })
    }
    
    self.pesquisar_por_token = function(numero_brinco, token){
        $scope.pesagens = [];
        self.show_list = false;
        pesagemService.query({
            gado__fazenda__access_token: token, 
            expand:'gado',
            gado__numero_brinco:numero_brinco
        }).then(function(response){
            $scope.pesagens = response.results;
            self.show_list = true;
        }, function(err){
            console.log('err')
        })
    }

    // gadoService.query({}).then(function(response){
    //     self.gados = response.results;
    //     console.log(self.pesagens)
    // }, function(err){
    //     console.log('err')
    // })

    $scope.$watch(function () {
        return self.pesagens
    }, function (newValue, oldValue) {
        if (newValue != oldValue) {
            console.log('>>>', newValue)
            oldValue = newValue;
        }
    });

})
    