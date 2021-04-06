function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function descuento(){
    var monto = parseInt(document.formulario.MontoCompra.value);

    var pago = monto-(monto*.15);

    document.formulario.total.value = "$" + pago;
}

function borrar(){
    document.formulario.MontoCompra.value = "";
    document.formulario.total.value = "";
}