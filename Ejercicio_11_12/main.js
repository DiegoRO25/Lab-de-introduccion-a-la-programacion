console.log("MAIN JS CARGADO");

let ultimoCodigoMostrado = "";

function revisarCodigo() {

    fetch("/obtener_codigo")
    .then(response => response.json())
    .then(data => {

        console.log("Respuesta:", data);

        if (
            data.codigo &&
            data.codigo !== "" &&
            data.codigo !== ultimoCodigoMostrado
        ) {

            const input = document.getElementById("codigoManual");

            if (input) {
                input.value = data.codigo;
            }

            ultimoCodigoMostrado = data.codigo;
        }
    })
    .catch(error => {
        console.log("ERROR:", error);
    });
}

setInterval(revisarCodigo, 1000);
