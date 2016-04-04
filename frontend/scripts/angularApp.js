angular
    .module('apiApp', [])
    .controller('apiAppCtrl', ['$http', controladorPrincipal]);

function controladorPrincipal($http) {
    var vm=this;

    // Realizamos un GET de todas las preguntas a mostrar
    $http.get("http://localhost:8000/preguntas.json").success(function(respuesta){
        vm.preguntas = respuesta;
        console.log(respuesta);
    });

    // Realiza un PUT sobre la API para cambiar la opcion seleccionada y establecer el salto
    vm.click = function(respuesta, opcion_seleccionada) {        
        if (!isNaN(parseFloat(opcion_seleccionada)) && isFinite(opcion_seleccionada)) {
            respuesta.opcion = opcion_seleccionada
            $http.put("http://localhost:8000/respuestas/" + respuesta.pk + ".json", respuesta)
                .success(function(respuesta) {
                    console.log(respuesta);
                });
        };
    }

    // Si salto es mayor a la pregunta que se le pasa devuelve false
    vm.salto = null
    vm.mostrar = function(first, pregunta) {
        if (first) {
            vm.salto = pregunta.salto
            return true
        }

        if (vm.salto > pregunta.pk){
            return false
        }

        vm.salto = pregunta.salto
        return true
    }
}