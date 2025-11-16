document.addEventListener("DOMContentLoaded", () => {

    const cant = cantidades; 
    const indices = {};

    // Inicializar todos los índices en 1 o según la configuración guardada
    Object.keys(cant).forEach(part => {
        indices[part] = avatarConfig[part] || 1;
    });

    // Función para mostrar la capa correcta
    function actualizarParte(part) {
        const imgs = document.querySelectorAll(`.avatar-layer[data-layer="${part}"]`);
        imgs.forEach((img, idx) => {
            img.style.display = (idx + 1 === indices[part]) ? "block" : "none";
        });

        const display = document.querySelector(`.control-group[data-part="${part}"] .current-index-display`);
        if (display) {
            display.textContent = `${indices[part]} / ${imgs.length}`;
        }
    }

    // Conectar botones
    document.querySelectorAll(".nav-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const part = btn.parentElement.dataset.part;
            const direction = parseInt(btn.dataset.direction);

            indices[part] += direction;
            const imgs = document.querySelectorAll(`.avatar-layer[data-layer="${part}"]`);
            if (indices[part] < 1) indices[part] = imgs.length;
            if (indices[part] > imgs.length) indices[part] = 1;

            actualizarParte(part);
        });
    });

    // Inicializar todas las partes
    Object.keys(cant).forEach(actualizarParte);

    // Guardar avatar por AJAX
    document.getElementById("guardar-avatar").addEventListener("click", () => {
        fetch("/gachalife/guardar/", { // URL fija de tu urls.py
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify(indices)
        })
        .then(response => response.json())
        .then(data => alert(data.status))
        .catch(err => console.error(err));
    });

    // Función para obtener CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});
