let isNightMode = false;

document.addEventListener("DOMContentLoaded", () => {
  const nightModeButtonDiv = document.querySelector(".night-mode-div");
  const body = document.querySelector("body");

  nightModeButtonDiv.addEventListener("click", () => {
    isNightMode = !isNightMode;
    
    if (isNightMode) {
      body.style.filter = "invert(1)"
      body.style.backgroundColor = "black"
    } else {
      body.style.filter = "invert(0)"
      body.style.backgroundColor = "white"
    }
  })
})