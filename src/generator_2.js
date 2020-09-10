let markers = document.getElementsByClassName('awesome-marker-icon-black');

for (let i = 0; i < markers.length; i++) {
  let marker = markers[i];
  marker.innerHTML = (i + 1);
}