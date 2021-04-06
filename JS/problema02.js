function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Salario(){
    //obtenemos los valores del formulario y los parseamos
    var salario1 = document.formulario.sueldobase.value;
    var ventas1 = document.formulario.ventas.value;

    var salario2 = parseInt(salario1);
    var ventas2 = parseInt(ventas1);
    
    //obtenemos sus comisones y salario total
    var comisiones = salario2*.1;
    var totalcomisiones = comisiones*ventas2;
    var sueldototal = salario2+totalcomisiones;

    //Se lo regresamos al usuario
    document.formulario.ComisionesTotales.value = "$" + totalcomisiones;
    document.formulario.salarioTotal.value = "$" + sueldototal;

}

function borrar(){
    document.formulario.sueldobase.value = "";
    document.formulario.ventas.value = "";
    document.formulario.ComisionesTotales.value = "";
    document.formulario.salarioTotal.value = "";
}