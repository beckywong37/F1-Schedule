from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Serve static files from static folder (for images in static folder)
app.static_folder = 'static'


# Automatically redirect to Home page from root URL
@app.route('/')
# Route to render Home page
@app.route('/home')
def home():
    # GET request to Ergast API to retrieve driver standings data
    url = 'http://ergast.com/api/f1/current/driverStandings.json'
    response = requests.get(url)
    # Print error status code for debugging purposes and error_handling.html for user
    if response.status_code != 200:
        print('Error:', response.status_code)
        # Error message will be printed in error_handling.html
        return render_template('error_handling.html', message='Failed to fetch data from API')

    # Store JSON response in variable "data"
    data = response.json()
    # Parse data for necessary headers and store in variable "standings_data"
    standings_data = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    # Display drivers standing in an HTML table
    standings_table_html = '<table>'
    # Define headers for table using <th>
    standings_table_html += '<tr><th>Position</th><th>Driver</th><th>Points</th></tr>'
    # Iterate through standings_data, add new row within table with requested data
    for index, driver in enumerate(standings_data, start=1):
        standings_table_html += f'<tr><td>{index}</td><td>{driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]}</td><td>{driver["points"]}</td></tr>'
    # Close table
    standings_table_html += '</table>'

    # Render the home page with the standings table
    return render_template('F1_Home.html', standings_table_html = standings_table_html)

# Route to render Teams HTML template
@app.route('/teams')
def teams():
    return render_template('F1_Teams.html')

# Route to render Schedule HTML template
@app.route('/schedule')
def schedule():
    return render_template('F1_Schedule.html')

# Create GrandPrix class to represent races in F1
class GrandPrix:
    def __init__(self, name, date, circuit, race_time, round, trackImg):
        """Constructor for creating instance of grand prix"""
        self.name = name
        self.date = date
        self.circuit = circuit
        self.race_time = race_time
        self.round = round 
        self.trackImg = trackImg

    def get_race_details(self):
        """Returns race details"""
        return {
            'name': self.name,
            'date': self.date,
            'circuit': self.circuit,
            'race_time': self.race_time,
        }

    def get_track_img(self):
        """Returns path for image of the race track"""
        return self.trackImg

# Create instances of GrandPrix
monacoGP = GrandPrix("Monaco GP", "May 24 - 26", "Circuit de Monaco", "Sat, May 25 @6:00 PM PST", 8, "images/monaco.png")
bahrainGP = GrandPrix("Bahrain GP", "Feb 28 - Mar 1", "Bahrain International Circuit", "Fri, Mar 1 @1:00 PM PST", 1, "images/bahrain.avif")
saudiGP = GrandPrix("Saudi Arabia GP", "Mar 7 - Mar 9", "Jeddah Street Circuit", "Fri, Mar 8 @1:00 PM PST", 2, "images/saudi.png")
australiaGP = GrandPrix("Australian GP", "Mar 22 - 24", "Melbourne Circuit", "Sun, Mar 24 @9:00 PM PST", 3, "images/austrilian.avif")
japanGP = GrandPrix("Japanese GP", "Apr 5 - 7", "Suzuka International Racing Course", "Sun, Apr 7 @10:00 PM PST", 4, "images/japan.avif")
chinaGP = GrandPrix("Chinese GP", "Apr 19 - 21", "Shanghai International Circuit", "Sun, Apr 21 @12:00 PM PST", 5, "images/china.avif")
usGP = GrandPrix("Miami GP", "May 3 - 5", "Miami International Autodrome", "Sun, May 5 @1:00 PM PST", 6, "images/miami.avif")
italyGP = GrandPrix("Italian GP", "May 17 - 19", "Autodromo Enzo e Dino Ferrari", "Sun, May 19 @6:00 AM PST", 7, "images/italian.png")
canadaGP = GrandPrix("Canada GP", "June 7 - 9", "Circuit Gilles-Villeneuve", "Sun, June 7 @11:00 AM PST", 9,"images/canada.avif")
spainGP = GrandPrix("Spain GP", "June 21 - 23", "Circuit de Barcelona-Catalunya", "Sun, June 23 @6:00 AM PST", 10, "images/spain.avif")
austriaGP = GrandPrix("Austria GP", "June 28-30", "Red Bull Ring", "Sun, June 30 @6:00 AM PST", 11, "images/austria.avif")
britainGP = GrandPrix("Great Britain GP", "July 5 - 7", "Silverstone Circuit", "Sun, July 7 @7:00 AM PST", 12, "images/greatbritain.avif")
hungaryGP = GrandPrix("Hungary GP", "July 19 - 21", "Hungaroring", "Sun, July 21 @6:00 AM PST", 13, "images/hungary.avif")
belgiumGP = GrandPrix("Belgium GP", "July 26 - 28", "Circuit de Spa-Francorchamps", "Sun, July 28 @6:00 AM PST", 14, "images/belgium.avif")
netherlandsGP = GrandPrix("Dutch GP", "August 23 - 25", "Circuit Zandvoort", "Sun, August 25 @6:00 AM PST", 15, "images/netherlands.avif")

# Create array for all instances of GPs
listGPs = [monacoGP, bahrainGP, saudiGP, australiaGP, japanGP, chinaGP, usGP, italyGP, canadaGP, spainGP, austriaGP, britainGP, hungaryGP, belgiumGP, netherlandsGP]

# Route to get race details when button is clicked
@app.route('/get_race_details')
def get_race_details():
    """Retrieves selected race from user, prints race details on webpage"""
    selected_race = request.args.get('selectedRace')

    # selected_race is a string, need the corresponding grand prix object
    # loop through listGPs, if selected_race matches name attribute
    # set object equal to variable selected_race_object
    selected_race_object = None
    for grand_prix in listGPs:
        if grand_prix.name == selected_race:
            selected_race_object = grand_prix
            break

    # Check if the Grand Prix was found, if found return race_details
    if selected_race_object is not None:
        race_details = {
            'name': selected_race_object.name,
            'date': selected_race_object.date,
            'circuit': selected_race_object.circuit,
            'race_time': selected_race_object.race_time,
        }
        return jsonify({'race_details': race_details})
    else:
        return jsonify({'error': 'Grand Prix not found'})

# Route to get race track when button is clicked
@app.route('/get_race_track')
def get_race_track():
    selected_race = request.args.get('selectedRace')

    # selected_race is a string, need the corresponding grand prix object
    selected_race_object = None
    for grand_prix in listGPs:
        if grand_prix.name == selected_race:
            selected_race_object = grand_prix
            break

    # Check if the Grand Prix was found, return path to track image
    if selected_race_object is not None:
        return jsonify({'track_img': selected_race_object.trackImg})
    else:
        return jsonify({'error': 'Grand Prix not found'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
