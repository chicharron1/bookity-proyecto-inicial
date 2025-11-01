function initMap() {
  const mapContainer = document.getElementById('map');

  const defaultLat = -33.03473;
  const defaultLng = -71.59688;

  // Si vienen coordenadas del usuario, úsalas
  const lat = (typeof latitud_defecto !== 'undefined' && latitud_defecto !== null) ? latitud_defecto : defaultLat;
  const lng = (typeof longitud_defecto !== 'undefined' && longitud_defecto !== null) ? longitud_defecto : defaultLng;

  // 1️⃣ Crear el mapa primero
  const map = L.map('map').setView([lat, lng], 16);

  // 2️⃣ Luego agregar la capa
  L.tileLayer(
    'https://api.maptiler.com/maps/streets-v2/256/{z}/{x}/{y}.png?key=EdWFsXtwOisU8uwq86cZ',
    {
      maxZoom: 19,
      minZoom: 1,
      attribution:
        '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
    }
  ).addTo(map);

  // 3️⃣ Definir variables de marcador y campos
  let marker;
  const latInput = document.getElementById('id_latitud')||document.getElementById('id_latitud_defecto');
  const lngInput = document.getElementById('id_longitud')||document.getElementById('id_longitud_defecto');

  // 4️⃣ Si hay valores iniciales, marcarlos
  if (latInput?.value && lngInput?.value) {
    const currentLat = parseFloat(latInput.value);
    const currentLng = parseFloat(lngInput.value);
    marker = L.marker([currentLat, currentLng]).addTo(map);
    map.setView([currentLat, currentLng], 16);
  }

  // 5️⃣ Al hacer clic en el mapa
  map.on('click', function (e) {
    const newLat = e.latlng.lat.toFixed(6);
    const newLng = e.latlng.lng.toFixed(6);

    if (marker) marker.setLatLng(e.latlng);
    else marker = L.marker(e.latlng).addTo(map);

    if (latInput) latInput.value = newLat;
    if (lngInput) lngInput.value = newLng;
  });
}