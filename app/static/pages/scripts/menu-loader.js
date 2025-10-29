function loadMenu() {
            fetch('components/menu.html')
                .then(response => response.text())
                .then(data => {
                    // Crear un elemento temporal para parsear el HTML
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = data;

                    // Obtener el aside
                    const sidebar = tempDiv.querySelector('aside');

                    if (!sidebar) {
                        console.error('No se encontró el aside en el menú.');
                        return;
                    }

                    // Reemplazar el placeholder con el aside
                    const placeholder = document.getElementById('sidebar-placeholder');
                    placeholder.replaceWith(sidebar);

                    // Marcar el menú activo según la URL actual
                    const currentPage = window.location.pathname.split('/').pop();
                    const menuLinks = document.querySelectorAll('.menu-item');
                    menuLinks.forEach(link => {
                        if (link.getAttribute('href') === currentPage) {
                            link.classList.add('menu-item--active');
                        }
                    });
                })
                .catch(err => console.error('Error al cargar el menú:', err));
        }
        // Cargar el menú cuando la página esté lista
        document.addEventListener('DOMContentLoaded', loadMenu);