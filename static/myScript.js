// When buttons are clicked, JavaScript code will executed
// JavaScript functions use 'fetch' API to send request to Flask server,
// receive the data, and display it on the webpage

// Function to iterate through listGPs
function printListofGPs () {
    for(const grandPrix of listGPs) {
        console.log(grandPrix.name)
    }
}

// Sends request to Flask with user selected GP, receives race details and displays on webpage
function showRaceDetails(endpoint) {
    // store user select race from dropdown menu in variable
    let userSelectGP = document.getElementById('selectRace').value;
    // fetch request sent to Flask with user selected race parameter
    fetch(`/${endpoint}?selectedRace=${userSelectGP}`)
        // converts response from Flask to JSON
        .then(response => response.json())
        .then(data => {
            // store output div element in a variable
            let outputRaceDetails = document.getElementById('raceDetailsOutput');
            // output will be race details and will update the output div element
            outputRaceDetails.innerHTML = `
                <p>Grand Prix: ${data.race_details.name}</p>
                <p>Date: ${data.race_details.date}</p>
                <p>Circuit Name: ${data.race_details.circuit}</p>
                <p>Race Start Time (PST): ${data.race_details.race_time}</p>
            `;
        })
        // Prints error on console
        .catch(error => console.error('Error:', error));
}

// Sends request to Flask with user selected GP, receives track image and displays on webpage
function showRaceTrack(endpoint) {
    // store user select race from dropdown menu in variable
    let userSelectGP = document.getElementById('selectRace').value;
    // Fetch the race track image from Flask
    fetch(`/${endpoint}?selectedRace=${userSelectGP}`)
        .then(response => response.json())
        .then(data => {

            // store the path to the track_img in variable
            let trackImgFilename = data.track_img;

            // Create an image element that will be displayed on webpage
            let imgElement = document.createElement('img');
            
            // Set the src attribute to path of the image file (in static folder)
            imgElement.src = `/static/${trackImgFilename}`;
            // Set other img attributes
            imgElement.alt = 'Race Track';
            imgElement.id = 'imgElement';

            // Get the output div and clear existing content
            let outputTrackImg = document.getElementById('raceTrackOutput');
            outputTrackImg.innerHTML = '';

            // Append the image element to the output div
            outputTrackImg.appendChild(imgElement);
        })
        .catch(error => console.error('Error:', error));
}
