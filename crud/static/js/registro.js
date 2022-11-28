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

$(function () // public static void main (JAVa)
{

  $("#btnGuardar").click(function () {
    let correo = document.getElementById("txtCorreo").value;
    let caracteres = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    var win = 0
    let temp = '';
      var reverseRut = $(".txtRut").val().split("").reverse().join("");
      var dv = $(".txtDV").val()
      var suma = 0;
      var serie = 2

      for (var i = 0; i < reverseRut.length; i++) {
        suma += serie * parseInt(reverseRut[i])
        serie++
        if (serie > 7){
          serie = 2
        }
       }
       var sumaDv = (11 - (suma - Math.trunc(suma/11)*11))
       if (dv == sumaDv || dv == '0' && sumaDv == '11'||  dv == 'k' && sumaDv== '10')
       {
         var dvValido = 1
       }


    if (!$(".txtRut").val() || $(".txtRut").val().length < 7 || !dvValido) {
      temp += 'rut, ';
    }
    if (!$(".txtNombre").val()) {
      temp += 'nombre, ';
    }
    if (!$(".txtApellido").val()) {
      temp += 'apellidos, ';
    }
    if (!caracteres.test(correo)) {
      temp += 'correo electronico, '
    }
    if(!$(".txtContrasenna"))
    {
      temp += 'contraseña, '
    }
    if ($(".txtContrasenna").val() != $(".txtContrasenna2").val()){
      temp += 'contraseñas distintas, '
    }
    if (!$(".txtDireccion").val()) {
      temp += 'direccion, ';
    }

    if (!$(".txtAnno").val()) {
      temp += 'fecha nacimiento, ';
    } else if($(".txtAnno").val() > 2004){
      temp += 'menor de 18 años ,'
    }

    if (!document.getElementById('checkbox-1').checked) {
      temp += 'terminos y condiciones';
    }
    if (temp != '') {
      alert('los siguientes campos son invalidos:\n' + temp)
      temp = '';
      return false
    }
    else if (temp == ''){
      alert('registro exitoso')
      win = 1
      function registro(){
        document.getElementsByClassName("precio")

      }
    }

  });
  let letras = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM ÁÉÍÓÚáéíóú';
  $(".formLetras").keypress(function (e) {
    let caracter = String.fromCharCode(e.which);
    if (letras.indexOf(caracter) < 0)
      return false;
  })
  let numeros = '0123456789';
  $(".txtRut").keypress(function (e) {
    let caracter = String.fromCharCode(e.which);
    if (numeros.indexOf(caracter) < 0)
      return false;
  })
  let dv = '0123456789Kk';
  $(".txtDV").keypress(function (e) {
    let caracter = String.fromCharCode(e.which);
    if (dv.indexOf(caracter) < 0)
      return false;
  })



  $(".flagd").click(function(){

  if (!$(".txtNtarjeta").val()) {
    temp += 'N° tarjeta, ';
  }
  if (!$(".txtVenc").val()) {
    temp += 'fecha vencimiento, ';
  }
  if (!$(".txtCVV").val()) {
    temp += 'CVV, ';
  }

  if (temp != '') {
    alert('los siguientes campos son invalidos:\n' + temp)
    temp = '';
  }
  else if (win == 0){
    alert('registro incompleto')
  }
  else if(temp == ''){
    alert("donacion registrada")
  }

  })

  

});

