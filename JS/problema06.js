function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Calcular_Edad(){
    
    var fecha = new Date();
    //Fecha que se obtiene de la computadora
    var Anio_actual = fecha.getFullYear();
    var Mes_actual = fecha.getMonth();

    //Fecha de nacimiento del usuario
    var Anio = parseInt(document.formulario.anio.value);
    var Mes = parseInt(document.formulario.mes.value);

    if(document.formulario.anio.value == ""){
        alert("Escriba un año");
    }else{
        var anios_usuario = Anio_actual-Anio;
        if(anios_usuario<=0){
            alert("Escriba un año válido");
        }else{
            var meses_usuario = Mes-Mes_actual;
            if(meses_usuario<=0){
                document.formulario.Edad.value = anios_usuario+" años";
            }else{
                anios_usuario = anios_usuario-1;
                document.formulario.Edad.value = anios_usuario+" años";
            }
        }
    }
}

function borrar(){
    document.formulario.anio.value = "";
    document.formulario.mes.value = "";
    document.formulario.Edad.value = "";
    
}