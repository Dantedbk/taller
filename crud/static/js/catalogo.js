// Anonymous "self-invoking" function
(function() {
    var startingTime = new Date().getTime();
    // Load the script
    var script = document.createElement("SCRIPT");
    script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
    script.type = 'text/javascript';
    document.getElementsByTagName("head")[0].appendChild(script);

    // Poll for jQuery to come into existance
    var checkReady = function(callback) {
        if (window.jQuery) {
            callback(jQuery);
        }
        else {
            window.setTimeout(function() { checkReady(callback); }, 20);
        }
    };

    // Start polling...
    checkReady(function($) {
        $(function() {
            var endingTime = new Date().getTime();
            var tookTime = endingTime - startingTime;
        });
    });
})();

var dolar = 0
let flag = 0



$.getJSON('https://mindicador.cl/api', function (data) {
var dailyIndicators = data;
dolar = dailyIndicators.dolar.valor
}).fail(function () {
console.log('Error al consumir la API!');
});

function updatep() {
flag += 1
var precios = document.getElementsByClassName("precio")
for (var i = 0; i < precios.length; i++) {
    var precio = precios[i].innerHTML;
    if (flag % 2 == 0) {
    temp = precio * dolar  
    precios[i].innerHTML = temp.toFixed(0);
    document.getElementById("switch").innerHTML = 'cambiar a USD';
    }
    else {
    temp = precio * 1 / dolar
    precios[i].innerHTML = temp.toFixed(2)
    document.getElementById("switch").innerHTML = 'cambiar a CLP';
    }
}

}
function refreshPage(){
    window.location.reload();
} 


async function tt_venta(){

    total = 0
    var totales = document.getElementsByClassName("tt_item")
    for (var i = 0; i < totales.length; i++) {
        var precio = totales[i].innerHTML;
        precio = precio.slice(1)
        total += parseInt(precio)
    }
    document.getElementById('tt_venta').innerHTML = 'Total: $' + total.toString()
}

