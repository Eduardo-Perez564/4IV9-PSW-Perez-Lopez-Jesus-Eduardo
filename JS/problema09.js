function validarn(e){
    var teclado = (document.all)?e.keycode:e.which;

    if(teclado == 8) return true;

    var patron = /[0-9\d]/;

    if(teclado == 8) return true;

    var prueba = String.fromCharCode(teclado);

    return patron.test(prueba);
}

function Calcular_Sueldo(){

    var sueldo = parseInt(document.formulario.sueldo.value);
    var Horas_Trabajadas = parseInt(document.formulario.Horas.value);
    var Horas_Extra1;
    var Horas_Extra2;
    var sueldoTotal;

    if(document.formulario.sueldo.value == "" || document.formulario.Horas.value == "" ){
        alert("Por favor, no deje campos vacíos");
    }else{
        if(Horas_Trabajadas>40){
            Horas_Extra1 = Horas_Trabajadas-40;
            if(Horas_Extra1>8){
                Horas_Extra2 = Horas_Extra1-8;
                sueldoTotal = (40*sueldo)+(8*sueldo*2)+(Horas_Extra2*sueldo*3);
                document.formulario.Total.value = "$" + sueldoTotal;
            }else{
                
                sueldoTotal = (40*sueldo)+(Horas_Extra1*sueldo*2);
                document.formulario.Total.value = "$" + sueldoTotal;
            }
        }else{
            sueldoTotal = Horas_Trabajadas*sueldo;
            document.formulario.Total.value = "$" + sueldoTotal;
        }
    }
}

function borrar(){
    document.formulario.sueldo.value = "";
    document.formulario.Horas.value = "";
    document.formulario.Total.value = "";
}