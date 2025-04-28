// Javascript turns elements with class "light" from white to red 

function startLights() {
  // selects all elements with class "light" and stores in lights variable
  const lights = document.querySelectorAll('.light');
  lights.forEach((light, index) => {
    // setTimeout adds delay before adding "red" class to lights
    setTimeout(() => {
      light.classList.add('red');
    }, index * 1000); // Adds 1 second delay 
  });

}

// Function is called when the webpage loads
window.onload = startLights;

// Play the F1 theme song
const audio = new Audio("/static/f1_theme.mp3");
const playButton = document.getElementById("playButton")
playButton.addEventListener("click", () => {
  audio.play();
});