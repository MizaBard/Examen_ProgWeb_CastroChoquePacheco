document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    // Obtener los valores de los campos
    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const telefono = document.getElementById("telefono").value;
    // Expresiones regulares
    const regexNombre = /^[a-zA-Z]{4,16}$/;
    const regexTelefono = /^[0-9]{10}$/;
    const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/; //extraido de w3 javascript utilizado en casi todos los correos


    // Validar el nombre
    if (nombre.trim() === "") {
        alert("Por favor, ingresa tu nombre.")
        return false;
    }
    else if (!regexNombre.test(nombre)){
        alert("El nombre debe contener 4 a 16 y solo letras")
        return false;
    }    

    // Validar el correo electrónico
    if (email.trim() ==="") {
        alert("Por favor, rellene el campo de correo electronico")
        return false;
    }
    else if (!regexEmail.test(email)){
        alert("Favor ingrese un correo electronico valido")
        return false;
    }    

    // Validar la contraseña
    if (password.trim()=== ""){
        alert("Por favor, rellene el campo de contraseña")
        return false;
    }
    else if (password.length < 8) {
        alert("La contraseña debe tener al menos 8 caracteres.");
        return false;
    }

    // Validar el teléfono
    if (telefono.trim()=== ""){
        alert("Por favor, rellene el campo de teléfono")
        return false;
    }
    else if (telefono < 9){
        alert("El numero de teléfono debe ser mayor a 9 dígitos")
    }
    else if (!regexTelefono.test(telefono)) {
        alert("Por favor, ingresa un número de teléfono válido (10 dígitos).");
        return false;
    }

    // Si todas las validaciones son exitosas, se puede enviar el formulario
    alert("Registro exitoso. ¡Bienvenido, " + nombre + "!");
    this.submit();
});

/*
// Función para validar el formato del correo electrónico
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}*/
