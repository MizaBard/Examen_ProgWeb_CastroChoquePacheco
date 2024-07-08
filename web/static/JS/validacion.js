function validarFormulario() {
    // Obtener los valores de los campos del formulario
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var commissionType = document.getElementById('commission-type').value;
    var paymentMethod = document.querySelector('input[name="payment-method"]:checked');

    // Verificar que todos los campos estén completos
    if (name === "" || email === "" || commissionType === "" || !paymentMethod) {
        alert("Por favor, completa todos los campos del formulario.");
        return false; // Detener el envío del formulario
        
    }

    // Verificar el formato del correo electrónico
    var emailRegex = /\S+@\S+\.\S+/;
    if (!emailRegex.test(email)) {
        alert("Por favor, introduce un correo electrónico válido.");
        return false; // Detener el envío del formulario
    }

    // Si todas las validaciones pasan, permitir el envío del formulario
    return true;
}
