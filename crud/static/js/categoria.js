$(function()
{
    $('.btnGuardar').click(function()
    {
        if(!$('.txtNombre').val())
        {
            alert("error");
        // $('.chkActivo').prop('checked', 'false');
            return false;
        }
    });
    $('.btnLimpiar').click(function()
    {
        $('.txtId').val('');
        $('.txtNombre').val('');
        $('.chkActivo').prop('checked', false);
        return false;
    });
});

var dolar = 0
    $.getJSON('https://mindicador.cl/api', function (data) {
      var dailyIndicators = data;
      dolar = dailyIndicators.dolar.valor
    }).fail(function () {
      console.log('Error al consumir la API!');
    });


    var temp;
    var normal;
    var flag = 0;
    var flag2 = 0;
    var precio = 0;
    
    function updatep() {
      precio = document.getElementById("precio").innerHTML
      if (flag2 == 0){
        normal = document.getElementById("precio").innerHTML
        temp = precio * 1 / dolar
        document.getElementById("precio").innerHTML = temp.toFixed(2)
      }
      else if (flag2 % 2 == 0) {
        temp = precio * 1 / dolar
        document.getElementById("precio").innerHTML = temp.toFixed(2)
        document.getElementById("switch").innerHTML = 'cambiar a CLP';
      }

      else {
        document.getElementById("precio").innerHTML= normal;
        document.getElementById("switch").innerHTML = 'cambiar a USD';
      }
      flag2 += 1
    }

    function desc(){
      precio = document.getElementById("precio").innerHTML
      var dcto = precio * 0.95
        if (flag == 0){
          normal = document.getElementById("precio").innerHTML
          document.getElementById("precio").innerHTML= dcto.toFixed(0);
        }
        else if (flag % 2 == 0){
          document.getElementById("precio").innerHTML= dcto.toFixed(0);
        }
        else{
          document.getElementById("precio").innerHTML= normal;
        }
        flag += 1
    }