function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Sacar_Porcentaje(){
    var Cantidad_Mujeres = parseInt(document.formulario.mujeres.value);
    var Cantidad_Hombres = parseInt(document.formulario.hombres.value);

    var Porcentaje_Mujeres = (Cantidad_Mujeres*100)/(Cantidad_Hombres+Cantidad_Mujeres);
    var Porcentaje_Hombres = (Cantidad_Hombres*100)/(Cantidad_Hombres+Cantidad_Mujeres);

    document.formulario.pmujeres.value = Porcentaje_Mujeres + "%";
    document.formulario.phombres.value = Porcentaje_Hombres + "%";
}

function borrar(){
    document.formulario.mujeres.value = "";
    document.formulario.hombres.value = "";
    document.formulario.pmujeres.value = "";
    document.formulario.phombres.value = "";
}