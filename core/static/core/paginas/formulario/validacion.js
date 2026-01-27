
document.addEventListener("DOMContentLoaded", function() {
    
    var form = document.getElementById("miFormulario");
    form.addEventListener("submit", function(event) {
        
        event.preventDefault();
        if (validarFormulario()) {
            window.location.href = window.location.href;
            alert("Formulario Enviado")
        }})
});


function validarFormulario() {
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var dni = document.getElementById("dni").value.trim();
    var correo = document.getElementById("correo").value.trim();
   

    
    if (nombre === "") {
        alert("Por favor ingresa tu nombre.");
        return false;
    }

    if (apellido === "") {
        alert("Por favor ingresa tu apellido.");
        return false;
    }

    if (dni === "") {
        alert("Por favor ingresa tu DNI.");
        return false;
    }

    if (correo === "") {
        alert("Por favor ingresa tu correo electrónico.");
        return false;
    }
   

    
    var nombreRegex = /^[a-zA-Z]+$/;
    if (!nombreRegex.test(nombre)) {
        alert("El nombre no debe contener números o simbolos extraños.");
        return false;
    }

    var apellidoRegex = /^[a-zA-Z]+$/;
    if (!apellidoRegex.test(apellido)) {
        alert("El apellido no debe contener númeroso simbolos extraños.");
        return false;
    }

  
    var dniRegex = /^\d+$/;
    if (!dniRegex.test(dni)) {
        alert("El DNI debe contener solo númeroso .");
        return false;
    }

    
    var archivo = document.getElementById("imagen").files[0];
    if (!archivo) {
        alert("Por favor selecciona un archivo.");
        return false;
    }

    return true; 
}

