function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d.]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Calcular_Utilidades(){
    var Salario = parseFloat    (document.formulario.salario.value);
    var Antiguedad = parseFloat(document.formulario.tiempo.value);
    var Utilidades;

    if(document.formulario.salario.value == "" || document.formulario.tiempo.value == ""){
        alert("Por favor, no deje campos vacíos");
    }else{
        if(Antiguedad < 1){
            Utilidades = Salario*.05;
            document.formulario.utilidades.value = "$"+Utilidades;
        }else if(Antiguedad >= 1 && Antiguedad < 2){
            Utilidades = Salario*.07;
            document.formulario.utilidades.value = "$"+Utilidades;
        }else if(Antiguedad >= 2 && Antiguedad < 5){
            Utilidades = Salario*.10;
            document.formulario.utilidades.value = "$"+Utilidades;
        }else if(Antiguedad >= 5 && Antiguedad < 10){
            Utilidades = Salario*.15;
            document.formulario.utilidades.value = "$"+Utilidades;
        }else{
            Utilidades = Salario*.20;
            document.formulario.utilidades.value = "$"+Utilidades;
        }
    }
}

function borrar(){
    document.formulario.utilidades.value = "";
    document.formulario.salario.value = "";
    document.formulario.tiempo.value = "";
}