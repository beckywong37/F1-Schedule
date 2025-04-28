Assignment: CS290 Final Project

Name: Becky Wong

Due Date: March 19, 2024

For my final project, I created a F1 informative website with multiple webpages, including ones from previous assignments as well as new ones I added for the final project.

I reorganized my code into 3 main folders:
- README_files: This includes this readme file about the final project, review of the 5 assignments, and review of the 5 websites I chose to review in the beginning of the term in assignment 1.
- static: includes images used in my websites, css styles, and any javascripts
- templates: includes html files for all webpages
Lastly, the flask_app.py is the main file that includes routes to different pages of my website and creates instances of "GrandPrixs" with routes to retrieve race details.

Here is what was refactored in my previous webpages:
- html files now include URLs of webpages in the "href" attribute to link horizontal navigation bar to these different pages
- flask_app.py includes routes to these different webpages
- added more GrandPrix races to the dropdown menu 

What is new:
- I finally added a home page to my website! I refactored the flask_app.py to include routes to the home page (both "/home" and "/"). Some components of the home page include:
    - 5 lights that, one by one, turn red to signify the start of the race. This starts right when the webpage is loaded.
    - A button to play the F1 Theme Song. I initially wanted to have the song play right when the webpage loaded, but decided that it wouldn't be the best user experience (could be disruptive, especially if the user isn't expecting it).
    - Current drivers standing. I used Ergast API to retrieve the drivers standing data, displayed it in an HTML table, and added it to the HTML for the home page. Cool to see the drivers standing update after the races as it grabs the data in real time.
    - Added error handling if GET request for Ergast API fails