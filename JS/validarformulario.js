function validar(formulario){

    alert("Bienvenida Emily :)")
    if(formulario.nombre.value.length < 5){
        
        alert("Escriba por lo menos 5 caracteres dentro del campo de nombre");
        formulario.nombre.focus();

        return false;
    }

    var checkOK = "QWERTYUIOPASDFGHJKLÑZXCVBNM" 
    + "qwertyuiopasdfghjklñzxcvbnm";

    var checkStr = formulario.nombre.value;

    var allvalid = true;

    for(var i = 0; i < checkStr.length; i++){
        var ch = checkStr.charAt(i);
        for(var j = 0; j < checkOK.length; j++){
            if(ch == checkOK.charAt(i))
                break;
        
            if(j == checkOK.length){
                allvalid = false;
                break;
            }
        }
        
    }

    if(!allvalid){
        alert("Escribe solo letras en el campo Nombre")
        formulario.nombre.focus();
        return false;
    }
    
    /*
    Para validar la entrada de la edad del usuario
    */

    if(formulario.nombre.value.length < 2){
        
        alert("No puede escribir más de dos digitos en el campo Edad");
        formulario.nombre.focus();

        return false;
    }
 
    var checkOK = "1234567890"

    var checkStr = formulario.edad.value;

    var allvalid = true;

    for(var i = 0; i < checkStr.length; i++){
        var ch = checkStr.charAt(i);
        for(var j = 0; j < checkOK.length; j++){
            if(ch == checkOK.charAt(i))
                break;
        
            if(j == checkOK.length){
                allvalid = false;
                break;
            }
        }
        
    }

    if(!allvalid){
        alert("Escribe solo números en el campo Edad")
        formulario.edad.focus();
        return false;
    }

    /*
    Para validar la entrada de un correo electrónico
    */

    var txt = formulario.email.value;

    var b = /^[^@?\s]+@[^@\.\s]+(\.[^@\.\s]+)+$/;

    alert("Email "+(b.test(txt)?"":" no ")+"válido");
    return b.test(txt);
}

