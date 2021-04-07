function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[{0-9\d .]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function sacarPromedio(){

    var Examen1 = parseInt(document.formulario.primera.value);
    var Examen2 = parseInt(document.formulario.segunda.value);
    var Examen3 = parseInt(document.formulario.tercera.value);
    var Examen_Final = parseInt(document.formulario.final.value);
    var Trabajo_Final = parseInt(document.formulario.trabajo.value);

    if(Examen1.isEm)
    //Calificaciones 
    var Parciales = ((Examen1+Examen2+Examen3)/3)*0.55;
    var Final = Examen_Final*0.30;
    var Trabajo = Trabajo_Final*0.15;
    var Calificacion = Parciales+Final+Trabajo;

    document.formulario.PFinal.value = Calificacion;
}

function borrar(){
    document.formulario.primera.value = "";
    document.formulario.segunda.value = "";
    document.formulario.tercera.value = "";
    document.formulario.final.value = "";
    document.formulario.trabajo.value = "";
    document.formulario.PFinal.value = "";
}