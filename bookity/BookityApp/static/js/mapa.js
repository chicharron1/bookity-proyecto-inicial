function initMap() {
  const mapContainer = document.getElementById('map');

  const defaultLat = -33.03473;
  const defaultLng = -71.59688;
  const radioInput = document.getElementById('id_radio_marcador');

  // Si vienen coordenadas del usuario, úsalas
  const lat = (typeof latitud_defecto !== 'undefined' && latitud_defecto !== null) ? latitud_defecto : defaultLat;
  const lng = (typeof longitud_defecto !== 'undefined' && longitud_defecto !== null) ? longitud_defecto : defaultLng;
  const defaultRadio = (typeof radio_defecto !== 'undefined' && radio_defecto !== null)
    ? radio_defecto
    : 500;

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

  // 4️⃣ Crear el marcador inicial (aunque no haya valores en los inputs)
  let initialLat, initialLng;

  // Si hay coordenadas en los inputs, usarlas
  if (latInput?.value && lngInput?.value) {
    initialLat = parseFloat(latInput.value);
    initialLng = parseFloat(lngInput.value);
  } else {
    // Si no hay, usar las coordenadas por defecto
    initialLat = lat;
    initialLng = lng;
    if (latInput) latInput.value = lat.toFixed(6);
    if (lngInput) lngInput.value = lng.toFixed(6);
  }

  // Crear el círculo
  marker = L.circle([initialLat, initialLng], {
    radius: defaultRadio,
    color: 'lightblue',
    fillColor: 'lightblue',
    fillOpacity: 0.5
  }).addTo(map);

  map.setView([initialLat, initialLng], 16);

  window.addEventListener('cambioRadio', (event) => {
  const nuevoRadio = parseFloat(event.detail.value);
  if (marker) marker.setRadius(nuevoRadio);
  });

  // 5️⃣ Al hacer clic en el mapa
  map.on('click', function (e) {
    const newLat = e.latlng.lat.toFixed(6);
    const newLng = e.latlng.lng.toFixed(6);

    if (marker) marker.setLatLng(e.latlng);
    else marker = L.circle(e.latlng, { radius: 50, color: 'lightblue', fillColor: 'lightblue', fillOpacity: 0.5 }).addTo(map);

    if (latInput) latInput.value = newLat;
    if (lngInput) lngInput.value = newLng;
  });

  if (radioInput) {
    radioInput.value = defaultRadio;
    const label = document.getElementById('radio_valor');
    if (label) label.textContent = defaultRadio;
  }
}