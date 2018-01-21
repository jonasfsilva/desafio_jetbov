
jetBov
.service('pesagemService', function($resource){
    var pesagem = {
        padrao: $resource('/api/pesagens/:id/', { id:'@id'},
            {patch: {method:'PATCH'}, query: {method:'GET'},
             put: {method: 'PUT'}, post:{method: 'POST'}}),
        }

    this.query = function(params, type_return){ 
        return new Promise(function(success, error){
            pesagem['padrao'].query(params).$promise.then(function(data){
                return success(data);
            }, function(err){
                if(err.data)
                    return err;
                return err;
            });

        });
    }

    this.get = function(id, params, type_return){
        return new Promise(function(success, error){
            params = params || {};
            params = Object.assign({}, { id: id }, params);
            pesagem['padrao'].get(params).$promise.then(function(data){
                return success(data);
            }, function(err){
                if(err.data)
                    return error(err);
                error_conexao(err);
                return error(err);
            });
        });
    }
    
})