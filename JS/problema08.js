function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Mayor(){
    var Primer_numero = parseInt(document.formulario.uno.value);
    var Segundo_numero = parseInt(document.formulario.dos.value);
    var Tercer_numero = parseInt(document.formulario.tres.value);

    if(document.formulario.uno.value==""){
        alert("Escriba el primer número");
        formulario.uno.focus();
    }else if(Segundo_numero==""){
        alert("Escriba el segundo número");
        formulario.dos.focus();
    }else if(Tercer_numero==""){
        alert("Escriba el tercer número");
        formulario.tres.focus();
    }else{
        if(Primer_numero>Segundo_numero && Primer_numero>Tercer_numero){
            document.formulario.Numero_Mayor.value = Primer_numero;
        }else if(Segundo_numero>Primer_numero && Segundo_numero>Tercer_numero){
            document.formulario.Numero_Mayor.value = Segundo_numero;
        }else if(Tercer_numero>Primer_numero && Tercer_numero>Segundo_numero){
            document.formulario.Numero_Mayor.value = Tercer_numero;
        }else{
            alert("Todos los numeros son iguales, pruebe con otros");
        }
    }
}

function borrar(){
    document.formulario.uno.value = "";
    document.formulario.dos.value = "";
    document.formulario.tres.value = "";
    document.formulario.Numero_Mayor.value = "";
}