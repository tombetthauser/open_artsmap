document.addEventListener("DOMContentLoaded", () => {
  let markers = document.getElementsByClassName('awesome-marker-icon-black');
  
  for (let i = 0; i < markers.length; i++) {
    let marker = markers[i];
    marker.innerHTML = (i + 1);
  }
  
  // let body = document.querySelector("body");
  // let controlDiv = document.querySelectorAll(".leaflet-control")[0];
  // let nightmodeButton = document.createElement("a");
  // nightmodeButton.innerHTML = `☼`;
  // nightmodeButton.classList += "nightmode-map-button"
  
  // nightmodeButton.addEventListener("click", () => {
  //   body.style.filter = `invert(${body.style.filter[7] == 1 ? 0 : 1})`;
  // })
  // controlDiv.appendChild(nightmodeButton)
}) 