function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Operaciones(){
    var Primer_numero = parseInt(document.formulario.primero.value);
    var Segundo_numero = parseInt(document.formulario.segundo.value);
    var Resultado;
    if(Primer_numero == Segundo_numero){
        Resultado = Primer_numero*Segundo_numero;
        document.formulario.Resultado_Operacion.value = Resultado;
    }else if (Primer_numero>Segundo_numero){
        Resultado = Primer_numero-Segundo_numero;
        document.formulario.Resultado_Operacion.value = Resultado;
    }else if(Segundo_numero>Primer_numero){
        Resultado = Primer_numero+Segundo_numero;
        document.formulario.Resultado_Operacion.value = Resultado;
    }
}

function borrar(){
    document.formulario.Resultado_Operacion.value = "";
    document.formulario.primero.value = "";
    document.formulario.segundo.value = "";
}