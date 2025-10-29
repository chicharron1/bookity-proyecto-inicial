document.addEventListener('DOMContentLoaded', function() {
  const mapContainer = document.getElementById('map');
  if (!mapContainer) return; // Si no hay mapa en esta vista, no hace nada

  // Centrar mapa (ejemplo: Santiago)
  const map = L.map('map').setView([-33.45, -70.66], 13);

  // Capa base idéntica a la que usas en publicaciones
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap',
  }).addTo(map);

  let marker;

  // Si existen campos de lat/lng en el formulario, úsalos
  const latInput = document.getElementById('id_latitud');
  const lngInput = document.getElementById('id_longitud');

  // Si ya hay coordenadas (por ejemplo, al editar), mostrarlas
  if (latInput?.value && lngInput?.value) {
    const lat = parseFloat(latInput.value);
    const lng = parseFloat(lngInput.value);
    marker = L.marker([lat, lng]).addTo(map);
    map.setView([lat, lng], 15);
  }

  // Al hacer clic en el mapa
  map.on('click', function(e) {
    const lat = e.latlng.lat.toFixed(6);
    const lng = e.latlng.lng.toFixed(6);

    if (marker) marker.setLatLng(e.latlng);
    else marker = L.marker(e.latlng).addTo(map);

    if (latInput) latInput.value = lat;
    if (lngInput) lngInput.value = lng;
  });
});
